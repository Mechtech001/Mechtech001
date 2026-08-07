<div align="center">

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:0f0f14,100:1a1a24&height=180&text=Aditya%20Sharma&fontColor=E8B978&fontSize=46&fontAlign=50&fontAlignY=40&desc=Backend-leaning%20full-stack%20developer&descAlign=50&descAlignY=65&descSize=16&descColor=8A8A9A&animation=fadeIn" width="100%"/>

<br/>

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=15&duration=2800&pause=1200&color=8A8A9A&center=true&vCenter=true&repeat=true&width=560&height=28&lines=B.Tech+CSE+%40+IIIT+Ranchi+%C2%B7+2023%E2%80%932027;GDG+UI%2FUX+Lead+%C2%B7+President%2C+Kriti+Club" alt="Typing SVG"/>

<br/><br/>

<a href="https://www.linkedin.com/in/aditya-sharma-516491321"><img src="https://img.shields.io/badge/LinkedIn-E8B978?style=for-the-badge&logo=linkedin&logoColor=0f0f14" /></a>
<a href="mailto:aditya16may@gmail.com"><img src="https://img.shields.io/badge/Email-E8B978?style=for-the-badge&logo=gmail&logoColor=0f0f14" /></a>
<a href="https://github.com/Mechtech001"><img src="https://img.shields.io/badge/GitHub-E8B978?style=for-the-badge&logo=github&logoColor=0f0f14" /></a>

</div>

<br/>

### <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=700&size=26&duration=1&pause=100000&color=E8B978&center=false&vCenter=true&width=200&height=40&lines=About" alt="About"/>

I build backend systems and try to actually understand what's happening under the hood rather than assembling them from tutorials. Right now that means: auth flows, message queues, database schema design, and the occasional 2am rabbit hole into why Docker networking doesn't work the way I assumed it would.

A few things about how I work:

- I'd rather ship something smaller that I fully understand than something bigger I copy-pasted my way through.
- I lead UI/UX at GDG on campus and run the Kriti Club — so alongside backend work, I spend a fair amount of time thinking about how things *look and feel*, not just how they run.
- Dark themes, minimal tooling, privacy-respecting software. If an app asks for a login it doesn't need, I'm already looking for the alternative.

**Currently open to internships** — backend-heavy, Node.js/Express or similar stacks preferred, but I adapt fast.

<br/>

### <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=700&size=26&duration=1&pause=100000&color=7FB3D5&center=false&vCenter=true&width=200&height=40&lines=Stack" alt="Stack"/>

<div align="center">

<img src="https://skillicons.dev/icons?i=js,ts,nodejs,express,react,mongodb,postgres,mysql,cpp,c,py,html,css,tailwind,docker,kubernetes,kafka,redis,go,git,github,vscode,figma,linux,npm,postman,aws&theme=dark" alt="Tech Stack"/>

</div>

<br/>

**Languages:** JavaScript · TypeScript · C++ · C · Python · SQL
**Frontend:** React · Tailwind CSS · HTML/CSS
**Backend:** Node.js · Express.js · Socket.io
**Databases:** MongoDB · PostgreSQL · MySQL · Redis
**Infra & Messaging:** Docker · Kubernetes · Apache Kafka · NGINX · AWS
**Auth & APIs:** JWT · OAuth2 · REST · RBAC · idempotent API design
**Tools:** Git · GitHub · VS Code · Postman · Figma · Linux
**Currently learning:** Go

<br/>

### <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=700&size=26&duration=1&pause=100000&color=E89B72&center=false&vCenter=true&width=650&height=40&lines=Projects+I%27d+actually+walk+you+through" alt="Projects"/>

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

<div align="center">

<img src="https://github-readme-stats-fast.vercel.app/api/streak?username=Mechtech001&theme=dark&hide_border=true&bg_color=0F0F14&title_color=E8B978&text_color=8A8A9A&icon_color=E8B978&border_color=1a1a24" width="48%"/>

<br/>

<img src="https://github-readme-stats-fast.vercel.app/api/top-langs?username=Mechtech001&layout=compact&langs_count=6&theme=dark&hide_border=true&bg_color=0F0F14&title_color=E8B978&text_color=8A8A9A&border_color=1a1a24" width="48%"/>

</div>

<br/>

### <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=700&size=26&duration=1&pause=100000&color=8FBF8F&center=false&vCenter=true&width=250&height=40&lines=Right+now" alt="Right now"/>

```
GDG UI/UX Lead        →  campus design systems + workshops
Kriti Club President  →  running the show for our college's cultural fest
```

<br/>

<div align="center">

<img src="https://img.shields.io/github/followers/Mechtech001?style=for-the-badge&logo=github&logoColor=0f0f14&label=Followers&labelColor=E8B978&color=1a1a24" height="32"/>
<img src="https://komarev.com/ghpvc/?username=Mechtech001&style=for-the-badge&color=E8B978&label=PROFILE+VIEWS&labelColor=1a1a24" height="32"/>

</div>

<br/>

<div align="center">
<sub>Usually awake and building past midnight</sub>
</div>
