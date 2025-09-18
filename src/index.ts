import { Hono } from "hono";
import { Bot, webhookCallback} from 'grammy';
import type { Env } from "./core/types";
import { createDB } from "./core/db";
import { telegramUserTable } from "./core/schema";
import { eq } from "drizzle-orm";



const app = new Hono<{Bindings: Env}>();

// for health check
app.get('/', async (c) => {
    return c.text('Telegram Bot is running! 🚀')
})

const createBot = (token: string, env: Env) => {
	const bot = new Bot(token, {botInfo:{"id":6566733898,"is_bot":true,"first_name":"carrot","username":"carrotcarrot_bot","can_join_groups":true,"can_read_all_group_messages":false,"supports_inline_queries":false,"can_connect_to_business":false,"has_main_web_app":false}});
	bot.command('start', (ctx) => ctx.reply('Hi!'));
	bot.on('message', (ctx) => ctx.reply('pong'));

    const db = createDB(env)

    bot.command('start', async (ctx) => {
        const userId = ctx.from?.id
        const username = ctx.from?.username
        const firstName = ctx.from?.first_name
        
        if (userId) {
            const existingUser = await db.select().from(telegramUserTable).where(eq(telegramUserTable.telegramId, userId.toString()));

            if (existingUser.length === 0) {
                await db.insert(telegramUserTable).values({
                    telegramId: userId.toString(),
                    username: username || null,
                    firstName: firstName || 'Unknown'
                })

                await ctx.reply(`欢迎! ${firstName}, 你已成功注册为我们的用户!  `)
            } else {
                await ctx.reply(`欢迎回来! ${firstName}, 你已成功登录!`)
            }
        }
    })

    bot.command('users', async (ctx) => {
        try {
            const users = await db.select().from(telegramUserTable)
            await ctx.reply(`当前注册用户数量: ${users.length}`)
        } catch (error) {
            await ctx.reply('获取用户数据时出错')
        }
    })

	return bot;
};

// telegram webhook
app.post('/webhook', async (c) => {
   const bot = createBot('6566733898:AAHvC5tYMl3dRzl-WrNmsdPYi81aL0nS0KY', c.env)
   const handleUpdate = webhookCallback(bot, 'cloudflare-mod')
   return await handleUpdate(c.req.raw)
})

export default app;