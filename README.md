
# 🚀 Python Apps — Codespaces Setup

This repository contains two Python-based applications ready to run in GitHub Codespaces:

- OpenAI Agent App
- OpenAI Assistant Chat Bot

---

## 🚀 Launch Codespaces

| Project | Launch |
| :------ | :----- |
| **OpenAI Agent App** | [![Open in Codespaces](https://github.com/codespaces/new?hide_repo_select=true&repo=972769025&skip_quickstart=true&ref=main&devcontainer_path=.devcontainer%2Fopenai-agent%2Fdevcontainer.json) |
| **OpenAI Assistant Chat Bot** | [![Open in Codespaces](https://github.com/codespaces/new?hide_repo_select=true&repo=972769025&skip_quickstart=true&ref=main&devcontainer_path=.devcontainer%2Fopenai-assistant-chatbot%2Fdevcontainer.json) |

> Ensure you have **GitHub Codespaces** enabled for your account.

---

## 📋 Project Details

### 🛠 OpenAI Agent App
A simple agent framework built using OpenAI APIs.

### 🤖 OpenAI Assistant Chat Bot
A chatbot assistant built on OpenAI's Assistant API, designed for interactive conversations.

---

## 🔑 Required Secrets

Before starting your Codespace, set the following GitHub **repository secrets**:

| Secret Name            | Description                                           | Documentation |
| :--------------------- | :---------------------------------------------------- | :------------ |
| `PAYPAL_CLIENT_ID`      | PayPal Sandbox Client ID                              | [Link](https://developer.paypal.com/dashboard/applications/sandbox) |
| `PAYPAL_CLIENT_SECRET`  | PayPal Sandbox Client Secret                          | [Link](https://developer.paypal.com/dashboard/applications/sandbox) |
| `OPENAI_API_KEY`        | OpenAI API Key                                         | [Link](https://platform.openai.com/account/api-keys) |
| `OPENAI_API_VERSION`    | OpenAI API Version                                     | [Link](https://platform.openai.com/docs) |

> 🚨 Secrets are automatically injected into the Codespace environment — no need for a `.env` file.

---

## ⚙️ Local Development (Optional)

If you want to run locally:

1. Install Python 3.11+.
2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set the required environment variables manually.
5. Run the app:
   ```bash
   python app.py
   ```

---

# 🎉 Happy Coding!

