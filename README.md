# My Teacher GPT

### Description

Introducing a project that will brighten your day and make learning a breeze! Meet My Teacher, GPT – your friendly companion for tackling even the trickiest questions with ease. Say goodbye to confusing explanations, as GPT excels at simplifying complex problems, making learning a joy for both kids and adults, including those with learning disabilities. Embrace a simpler way to understand and excel in any subject!"


### Instructions

Under `user input` type in your question, and click submit.

Then, learn from a response thats much simpler to understand!

### ChatBot interface

![Alt Text](https://github.com/rishiselvakumaran98/MyTeacherGPT/blob/main/Doc/Images/ChatBot_Gui.png)

### Pre-requisite before running app locally
Install docker in your machine

### Running the app locally

1. Git clone this branch under `Code` -> `HTTPS` --> copy the link
2. In your local machine find a file directory and then do git clone <url>
3. `cd MyTeacherGPT`
4. Create a `.env` file at the root directory
5. Add `API_KEY=<open_ai_key>`
6. `docker build -t myteachergpt .`
7. `docker run -it -p 7860:7860 myteachergpt`
8. Open the url generated from the output (eg. http://0.0.0.0:7860)
9. Voila!!

