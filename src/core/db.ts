// src/db/index.ts
import { drizzle } from 'drizzle-orm/d1';
import * as schema from "./schema";
import type { Env } from "./types";

export function createDB(env: Env) {
  const db = drizzle(env.DB, { schema });
  return db;
}