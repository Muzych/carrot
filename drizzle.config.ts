import { defineConfig } from 'drizzle-kit';

export default defineConfig({
  schema: './src/core/schema.ts',
  out: './migrations',
  dialect: 'sqlite',
  driver: 'd1-http',
  dbCredentials: {
    databaseId: 'cdfacffd-f5c2-47fd-bd5a-f1a2616ef9e8', // 你的 D1 数据库 ID
  }
});
