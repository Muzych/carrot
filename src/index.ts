import { Hono } from "hono";
import { Bot, webhookCallback} from 'grammy';


const app = new Hono<{Bindings: Env}>();

app.post('/', async (c) => {
   
})

export default app;