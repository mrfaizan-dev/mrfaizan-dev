<p align="center">
  <img src="assets/hero-banner.gif" alt="Mr Faizan — Python Backend and Applied AI Developer" width="100%" />
</p>

<p align="center">
  <strong>Applied AI · Python Backend Engineering · Intelligent Automation</strong>
  <br />
  <a href="mailto:pakmrfaizan@gmail.com">Email</a>
  &nbsp;·&nbsp;
  <a href="https://github.com/mrfaizan-dev">GitHub</a>
  &nbsp;·&nbsp;
  <a href="https://github.com/mrfaizan-dev?tab=repositories">All repositories</a>
</p>

I build practical AI-powered systems that connect **LLMs, agent workflows, retrieval pipelines, browser automation, and Python backend services**. My focus is on turning unstructured web and document data into useful, validated outputs—not just standalone prompts or chat demos.

<p align="center">
  <a href="#selected-projects">Explore projects</a>
  &nbsp;·&nbsp;
  <a href="#technical-toolkit">Technical toolkit</a>
  &nbsp;·&nbsp;
  <a href="#contact">Contact</a>
</p>

---

## About

I'm **Mr Faizan**, a Python Backend and Applied AI Developer. I design and build end-to-end applications across four connected areas:

- **Agentic AI:** multi-step workflows that coordinate specialized agents, tools, and model calls.
- **RAG and document intelligence:** retrieval systems that ground LLM responses in documents and indexed knowledge.
- **Web research and automation:** browser-based extraction pipelines that turn public web pages into structured information.
- **Backend and data engineering:** asynchronous APIs, background workers, validation, processing, and export pipelines.

My primary engineering focus is the **Python backend and AI pipeline**. I also build application interfaces with **Next.js, React, and Tailwind CSS using AI-assisted frontend workflows**.

## What I Build

| Focus | What it means in practice |
| --- | --- |
| **Agentic AI applications** | LangGraph workflows, tool use, multi-stage reasoning, independent review, and human approval checkpoints. |
| **RAG and knowledge systems** | Document ingestion, embeddings, vector retrieval, BM25, rank fusion, reranking, and source-grounded answers. |
| **Intelligent web automation** | Playwright/Selenium-based browser workflows, retrieval fallbacks, site-specific parsers, and structured extraction. |
| **Python backend systems** | FastAPI services, Pydantic validation, asyncio, Celery workers, Redis queues, and Docker-based deployment. |
| **Data products** | Cleaning and validating extracted information, then delivering it through APIs, dashboards, Excel, and CSV. |

## Selected Projects

<p align="center">
  <img src="assets/portfolio-map.svg" alt="Overview of four applied AI and Python engineering projects" width="100%" />
</p>

<table>
  <tr>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/mrfaizan-dev/Autonomous-RFP-Pipeline">01 · Autonomous RFP Pipeline</a></h3>
      <p><strong>Agentic proposal automation with evidence and human review.</strong></p>
      <p>Turns a public RFP or project URL into a tailored proposal draft. The workflow extracts requirements, retrieves relevant portfolio evidence, drafts the response, sends it through an independent AI critique, and pauses for human approval.</p>
      <p><strong>Engineering highlights</strong><br />LangGraph orchestration · Portfolio RAG · Analyst / Writer / Critic agents · Revision loop · Human approval · Checkpointed workflow</p>
      <p><sub>Python · FastAPI · LangGraph · LlamaIndex · ChromaDB · Celery · Redis · Next.js</sub></p>
      <p><a href="https://github.com/mrfaizan-dev/Autonomous-RFP-Pipeline">Repository</a> &nbsp;·&nbsp; <a href="https://rfpaiagent.vercel.app/">Live application (AegisIQ)</a></p>
    </td>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/mrfaizan-dev/Enterprise-RAG-AI">02 · Enterprise RAG AI</a></h3>
      <p><strong>Hybrid document retrieval and cited question answering.</strong></p>
      <p>Turns PDF, TXT, and CSV files into searchable knowledge. Semantic retrieval and BM25 keyword search are combined with Reciprocal Rank Fusion, then Cohere reranking selects context for grounded LLM answers.</p>
      <p><strong>Engineering highlights</strong><br />Document ingestion · Gemini embeddings · ChromaDB · Hybrid retrieval · RRF · Cohere reranking · Source citations · Optional Celery queue</p>
      <p><sub>Python · FastAPI · LlamaIndex · ChromaDB · Gemini · Groq · Cohere · Celery · Redis</sub></p>
      <p><a href="https://github.com/mrfaizan-dev/Enterprise-RAG-AI">Repository</a></p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/mrfaizan-dev/CogniPulse-AI-Market-Intelligence">03 · CogniPulse</a></h3>
      <p><strong>Autonomous web research and market intelligence.</strong></p>
      <p>Converts a natural-language research question into a structured Markdown report. Tavily discovers relevant public URLs; a layered browser engine retrieves pages; LLM extraction is validated against Pydantic schemas.</p>
      <p><strong>Engineering highlights</strong><br />LangGraph Searcher / Scraper / Finalizer · Tavily search · Multi-engine retrieval · Structured extraction · Background research jobs</p>
      <p><sub>Python · FastAPI · LangGraph · Tavily · Playwright · SeleniumBase · Nodriver · Celery · Redis · Next.js</sub></p>
      <p><a href="https://github.com/mrfaizan-dev/CogniPulse-AI-Market-Intelligence">Repository</a></p>
    </td>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/mrfaizan-dev/Natural-Scraping-AI">04 · Natural Scraping AI</a></h3>
      <p><strong>Asynchronous multi-engine web scraping and data extraction.</strong></p>
      <p>Processes e-commerce and real-estate URLs through browser automation, fallback retrieval, site-specific parsers, structured validation, and data cleaning. Results can be exported as formatted Excel and CSV files, with optional PostgreSQL storage.</p>
      <p><strong>Engineering highlights</strong><br />Three-tier retrieval fallback · 12 listed site-specific parsers · Pydantic models · Pandas processing · Celery task tracking · Downloadable reports</p>
      <p><sub>Python · FastAPI · Playwright · SeleniumBase · Nodriver · BeautifulSoup4 · Pandas · Celery · Redis · PostgreSQL · Docker</sub></p>
      <p><a href="https://github.com/mrfaizan-dev/Natural-Scraping-AI">Repository</a></p>
    </td>
  </tr>
</table>

## Engineering Workflow

A recurring pattern across my projects is to move from raw inputs to useful, reviewable outputs through retrieval, orchestration, and validation. The exact pipeline varies by application.

<p align="center">
  <img src="assets/workflow-loop.gif" alt="Animated five-stage applied AI engineering workflow: collect, retrieve, orchestrate, validate, deliver" width="100%" />
  <br />
  <sub><a href="assets/workflow-map.svg">View the static workflow diagram</a></sub>
</p>

## Technical Toolkit

### Python and backend engineering

`Python` · `FastAPI` · `asyncio` · `Pydantic v2` · `Pandas` · `BeautifulSoup4` · `Celery` · `Redis` · `Docker` · `PostgreSQL` · `SQLite`

### Agentic AI and LLM applications

`LangGraph` · `LangChain` · `LlamaIndex` · `CrewAI` · `LLMs` · `Prompt Engineering` · `MCP`

### RAG, retrieval, and vector search

`RAG` · `Hybrid Search` · `BM25` · `Reciprocal Rank Fusion (RRF)` · `CRAG` · `ChromaDB` · `FAISS` · `Cohere Reranking`

### Browser automation and web data extraction

`Playwright` · `Selenium` · `SeleniumBase` · `Nodriver` · `BeautifulSoup4` · `Proxy Rotation` · `Multi-site Scraping` · `Structured Data Extraction`

### Evaluation, observability, and safeguards

`Langfuse` · `DeepEval` · `Guardrails`

### Model providers and AI assistants

**APIs / providers:** `OpenAI` · `OpenRouter` · `Groq` · `Google Gemini`  
**AI assistants:** `ChatGPT` · `Claude` · `Gemini`

### Frontend and UI development

`Next.js` · `React` · `Tailwind CSS` — built with AI-assisted frontend workflows; my main focus remains Python, backend systems, and applied AI.

## Engineering Principles

- **Ground outputs in evidence:** use retrieved documents or source pages where the task requires factual answers.
- **Validate at system boundaries:** use schemas and structured models instead of trusting free-form model output.
- **Design for long-running work:** move scraping and research tasks into background workers when they should not block API requests.
- **Plan for retrieval failures:** use retries, fallbacks, and explicit error paths where external sites or services are unreliable.
- **Keep humans in control:** use review and approval checkpoints when generated content needs a person to make the final decision.

## Contact

I'm interested in connecting with teams working on **Python backend engineering, Applied AI, agentic workflows, RAG systems, and intelligent automation**.

- **Email:** [pakmrfaizan@gmail.com](mailto:pakmrfaizan@gmail.com)
- **GitHub:** [github.com/mrfaizan-dev](https://github.com/mrfaizan-dev)

<p align="center">
  <img src="assets/footer-signature.svg" alt="Reliable pipelines. Grounded answers. Clean data. — Mr Faizan" width="100%" />
</p>
