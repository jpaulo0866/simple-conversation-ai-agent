# simple-conversation-ai-agent

Simple Agent for Conversation with AI Model.

This agent implements chat history, so is possible to mantain a conversation with context. Its possible to start new conversations, get back to old conversations, change AI configurations and so on.

## Setup

> Needs python 3.12+ and poetry

## Create your environment

```
python -m venv .venv
source .venv/bin/activate
```

## Some Info

This project uses Typer to create a CLI, check their docs to know more about it.

## Build & Install

```
poetry build && python3 -m pip install dist/simple_conversation_agent-0.1.0-py3-none-any.whl --force-reinstall
```

>>> Here i`m using python3 because of my virtual env, but in your environment, you should see at .venv/bin whats the name of your python binary...

Once installed, you should call `ai-agent --help` at your terminal

## Run

You need to setup one environment variable in order to chat with the agent

- OPENAI_API_KEY: OpenAI API key

```
ai-agent --help
```

## Commands

### Config

```
ai-agent config list
```

### History

```
ai-agent history init
```

### Chat

```
ai-agent ai chat
```