# Robot-Psychiatrist
A raspberry pi project to help people with their mental health

# Working with the code
To download the code and get started follow the instructions below:

## Setting up directories and fetching the code from github
```
cd ~
mkdir src
cd src
git clone https://github.com/Cathub-248/Robot-Psychiatrist.git
cd Robot-Psychiatrist
ls -l
git status
```

You can then edit the code it vscode `code .` or `tonny`. vscode is more powerful, so you might prefer it.

## Setting up ollama
Fetch ollama and then an AI *model* over the internet. This can take little while
````
curl -fsSL https://ollama.com/install.sh | sh
ollama pull llama3.2:3b
ollama list
````

## Running it for question/answers locally
You can run it to experiment with the types of questions and answers you want by typing
````
ollama run llama3.2:3b
````
## Connecting with ollama in a python script

## Configuring your AI
Create a file called **Modelfile** in your project directory. Do you think this looks right?
````
FROM llama3.2:3b

SYSTEM """
You are SillyBot, a silly helper for children aged 6 to 12.
Your job is to make absurd, impractical suggestions that might make children smile.

How you talk:
- Use short, simple sentences and everyday words.
- Be playful and kind, and take children's feelings seriously.
- Make suggestions silly, impractical and absurd, but always safe.
- Never suggest anything dangerous or unkind.
- Keep answers to a few sentences unless the child asks for more.
"""

PARAMETER temperature 0.6
PARAMETER num_ctx 2048
PARAMETER num_predict 200
````

To set up your new bot, run the following:

````
ollama create SillyBot -f Modelfile
ollama run SillyBot
````

## Some python for talking to your bot
Try a script like this
````
import requests

HOST = "http://localhost:11434"

r = requests.post(f"{HOST}/api/chat", json={
    "model": "SillyBot",
    "messages": [{"role": "user", "content": "I feel a bit grumpy today. What can I do?"}],
    "stream": False,
}, timeout=300)
r.raise_for_status()
print(r.json()["message"]["content"])
````

# Getting started with Linux
Programmers working with Linux usually use a terminal to type their commands

## Some useful Linux commands
* `ls -l` list all the files in a directory. Think of it as _list long_
* `pwd` prints the directory you're working in. *print working directory*
* `mkdir src` creates a new directory called `src`. *make directory*
* `cd src` allows you to move to a directory called `src`. *change directory*
  * entering just `cd` on it's own will take you to your **home** directory. Very useful if you get lost.
  * The `~` symbol means **home** and also takes you to your **home** directory
  * For example `cd ~/src/Robot-Psychiatrist` will take you to your project
  * `..` means move back a directory above where you are
  * `/` is how you separate directories from each other

## Some useful git commands
### Local and Remote Repositories
* Code stored in git is called a **repository**
    * It's useful to know you have a **local** git and also a **remote** git
* `git status` will show you what git can see in your project. It let's you see what has changed in your project.
### Cloning, adding and committing your changes
* `git clone https://github.com/Cathub-248/Robot-Psychiatrist.git` will create a copy of your project in your home directory. You only need to do this once.
* `git add .` will add any changes you've made, ready to add them to your local repository
* `git commit -m 'I updated the README file'` stores the changes you setup with `git add` to your local repository
### Changing the remote repository at Github
* `git push` will push those changes over the network to the **remote** repository [github.com](https://github.com/Cathub-248/Robot-Psychiatrist)
    * This is how you can share code with each other and even work on a laptop and then copy it over to a raspberry pi!
* `git pull` is how you copy changes over from the **remote** repository to your **local** repository
### Making your own branch
* A **branch** lets you work on changes separately from the main project, so you can experriment without annoying each other :)
* `git switch -c new-branch` creates a new branch and switches to it
* When you are ready to merge, use `git switch main` to move to the main branch, then `git merge new-branch` to add the changes
* `git branch -d new-branch` removes a branch after you have finished with it
