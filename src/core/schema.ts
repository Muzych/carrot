// src/schema.ts
import { relations } from 'drizzle-orm';
import { int, sqliteTable, text } from 'drizzle-orm/sqlite-core';

export const userTable = sqliteTable('user_table', {
  id: int().primaryKey({ autoIncrement: true }),
  name: text().notNull(),
});

export const postTable = sqliteTable('post_table', {
  id: int().primaryKey({ autoIncrement: true }),
  title: text().notNull(),
  content: text().notNull(),
  userId: int().references(() => userTable.id),
});

export const telegramUserTable = sqliteTable('telegram_users', {
  id: int().primaryKey({ autoIncrement: true }),
  telegramId: text('telegram_id').notNull().unique(),
  username: text('username'),
  firstName: text('first_name').notNull(),
  createdAt: int('created_at', { mode: 'timestamp' }).notNull().$defaultFn(() => new Date()),
});

export const userRelations = relations(userTable, ({ many }) => ({
  posts: many(postTable),
}));

export const postRelations = relations(postTable, ({ one }) => ({
  user: one(userTable, {
    fields: [postTable.userId],
    references: [userTable.id],
  }),
}));