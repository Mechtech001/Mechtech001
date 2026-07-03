<div align="center">

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:0f0f14,100:1a1a24&height=180&text=Aditya%20Sharma&fontColor=E8B978&fontSize=46&fontAlign=50&fontAlignY=40&desc=Backend-leaning%20full-stack%20developer&descAlign=50&descAlignY=65&descSize=16&descColor=8A8A9A&animation=fadeIn" width="100%"/>

<br/>

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=15&duration=2800&pause=1200&color=8A8A9A&center=true&vCenter=true&repeat=true&width=560&height=28&lines=B.Tech+CSE+%40+IIIT+Ranchi+%C2%B7+2023%E2%80%932027;GDG+UI%2FUX+Lead+%C2%B7+President%2C+Kriti+Club" alt="Typing SVG"/>

<br/><br/>

<a href="https://www.linkedin.com/in/aditya-sharma-516491321"><img src="https://img.shields.io/badge/LinkedIn-1a1a24?style=for-the-badge&logo=linkedin&logoColor=E8B978" /></a>
<a href="mailto:aditya16may@gmail.com"><img src="https://img.shields.io/badge/Email-1a1a24?style=for-the-badge&logo=gmail&logoColor=E8B978" /></a>
<a href="https://github.com/Mechtech001"><img src="https://img.shields.io/badge/GitHub-1a1a24?style=for-the-badge&logo=github&logoColor=E8B978" /></a>

</div>

<br/>

## About

I build backend systems and try to actually understand what's happening under the hood rather than assembling them from tutorials. Right now that means: auth flows, message queues, database schema design, and the occasional 2am rabbit hole into why Docker networking doesn't work the way I assumed it would.

A few things about how I work:

- I'd rather ship something smaller that I fully understand than something bigger I copy-pasted my way through.
- I lead UI/UX at GDG on campus and run the Kriti Club — so alongside backend work, I spend a fair amount of time thinking about how things *look and feel*, not just how they run.
- Dark themes, minimal tooling, privacy-respecting software. If an app asks for a login it doesn't need, I'm already looking for the alternative.

**Currently open to internships** — backend-heavy, Node.js/Express or similar stacks preferred, but I adapt fast.

<br/>

## Stack

<div align="center">

<img src="https://skillicons.dev/icons?i=js,ts,nodejs,express,react,mongodb,postgres,mysql,cpp,python,html,css,tailwind,docker,git,figma,linux,postman,aws&theme=dark" alt="Tech Stack"/>

</div>

<br/>

**Core:** Node.js · Express.js · MongoDB · TypeScript · React
**Expanding into:** Go, Apache Kafka, Redis, Docker, Kubernetes
**Auth & APIs:** JWT · OAuth2 · REST · RBAC · idempotent API design

<br/>

## Projects I'd actually walk you through

Not a list of every repo — just the ones where I made real decisions and hit real problems.

<br/>

<table>
<tr>
<td width="33%" valign="top">

**[Ledger](https://github.com/Mechtech001/Ledger)**
<br/>
Financial backend

A transaction system spanning 8 database models, with JWT auth and role-based access for 3 user roles. The interesting part wasn't the CRUD — it was making the API idempotent so retried requests can't double-charge someone, and wiring up OAuth2 email alerts that don't feel bolted on.

`Node.js` `Express` `MongoDB` `JWT`

</td>
<td width="33%" valign="top">

**[DevTinder](https://github.com/Mechtech001/DevTinder)**
<br/>
Developer networking platform

15+ REST endpoints across 10 schemas, real-time chat over WebSockets, and a premium-subscription flow with Razorpay in the loop. This is where I first had to think seriously about schema relationships instead of just making them work.

`Socket.io` `Razorpay` `AWS SES` `MongoDB`

</td>
<td width="33%" valign="top">

**[distributed-ticket-service](https://github.com/Mechtech001/distributed-ticket-service)**
<br/>
Event-driven backend

Built this specifically to stop treating "microservices" as a buzzword. A React client fires a request, Kafka queues it, a worker processes it and writes to Mongo, and a WebSocket pushes the result back — no polling. Docker taught me the hard way that `localhost` inside a container isn't `localhost` on your machine.

`Kafka` `Docker` `Socket.io` `NGINX`

</td>
</tr>
</table>

<br/>

> Full write-ups with architecture diagrams and "what I got wrong" notes live in each repo's README — I keep those honest on purpose.

<br/>

## Right now

```
GDG UI/UX Lead        →  campus design systems + workshops
Kriti Club President  →  running the show for our college's cultural fest
```

<br/>

<div align="center">

<img src="https://github-readme-stats.vercel.app/api?username=Mechtech001&show_icons=true&theme=dark&hide_border=true&bg_color=0f0f14&title_color=E8B978&icon_color=E8B978&text_color=8A8A9A" height="165"/>
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=Mechtech001&layout=compact&theme=dark&hide_border=true&bg_color=0f0f14&title_color=E8B978&text_color=8A8A9A" height="165"/>

</div>

<br/>

<div align="center">
<sub>Based in Rewari, Haryana · Usually awake and building past midnight</sub>
</div>
