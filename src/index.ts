import { Hono } from 'hono';
import { Bot, webhookCallback } from 'grammy';
import type { Env } from './core/types';

const app = new Hono<{ Bindings: Env }>();

app.get('/', async (ctx) => {
	return ctx.text('Telegram Bot is running! 🚀');
});

app.post('/webhook', async (ctx) => {
	const bot = new Bot(ctx.env.TELEGRAM_BOT_TOKEN);

	// 修复：使用不同的变量名，添加 async/await
	bot.on('message', async (botCtx) => {  // 改为 botCtx 避免冲突
		try {
			// 检查是否有文本内容
			if (botCtx.message.text) {
				await botCtx.reply('Hello! I received your message: ' + botCtx.message.text);
			} else {
				await botCtx.reply('Hello! I received your message (non-text)');
			}
		} catch (error) {
			console.error('Error replying to message:', error);
		}
	});

	// 添加错误处理
	bot.catch((err) => {
		console.error('Bot error:', err);
	});

	const handleUpdate = webhookCallback(bot, 'cloudflare-mod');
	return await handleUpdate(ctx.req.raw);
});

export default app;