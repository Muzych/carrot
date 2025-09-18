import { Hono } from 'hono';
import { Bot, webhookCallback } from 'grammy';
import type { Env } from './core/types';

const app = new Hono<{ Bindings: Env }>();



app.get('/', async (ctx) => {
	return ctx.text('Telegram Bot is running! 🚀');
});

app.post('/webhook', async (ctx) => {
	const bot = new Bot(ctx.env.TELEGRAM_BOT_TOKEN);

	bot.on('message', async (ctx) => {
		await ctx.reply('Hello! I received your message: ' + ctx.message.text);
	});

	const handleUpdate = webhookCallback(bot, 'cloudflare-mod');
	return await handleUpdate(ctx.req.raw);
})



export default app;
