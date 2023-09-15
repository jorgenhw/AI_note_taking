<!-- PROJECT LOGO -->
<br />
<p align="center">
  
  <h1 align="center">Your AI Note Mate</h1> 
  <h3 align="center">Cognitive Science Master's 2023</h3> 


  <p align="center">
    Jørgen HW
    <br />

  </p>
</p>


<!-- ABOUT THE PROJECT -->
## About the project 🤷‍♂️
In short, this script does three things: 1) It converts speech to text using [OpenAI's Whisper](https://openai.com/research/whisper), 2) it reformats this text into different formats (e.g. ELI5, main points, summary) using [OpenAI's GPT-3](https://beta.openai.com/signup/), and 3) it saves these conversions in a .txt file in the output folder, which can be used as a supplement to your own note-taking.

This is a very, very simple little sketch that I do not take any personal pride in, as I'm just putting already made material together. Please do not hesitate to suggest improvements either mouth to mouth or via a pull request ♥️

<!-- USAGE -->
## Usage ✅
To use or reproduce the results you need to adopt the following steps. Per default the scripts points to a sample audio file in the ```audio_files``` folder. If you want to use the script on something real, remember to change the path.

**NOTE:** There may be slight variations depending on the terminal and operating system you use. The following example is designed to work using the Visual Studio Code version 1.76.0 (Universal) on a machine running MacOS Ventura 13.4 on a M1 Max chip. The terminal code should therefore work using a unix-based bash. The avoid potential package conflicts, the ```setup.sh``` bash files contains the steps necesarry to create a virtual environment for the project.

1. Download ffmpeg
2. Clone repository
3. Update the ```.env``` file
4. Run setup.sh


> **Step 1** Download ```ffmpeg```

Using Whisper requires the command-line tool ffmpeg to be installed on your system, which is available from most package managers:

```
# on MacOS using Homebrew (https://brew.sh/)
brew install ffmpeg

# on Windows using Chocolatey (https://chocolatey.org/)
choco install ffmpeg

# on Windows using Scoop (https://scoop.sh/)
scoop install ffmpeg
```

> **Step 2** Clone repository

Clone repository using the following lines in the unix-based bash:

```bash
git clone https://github.com/jorgenhw/AI_note_taking.git
cd AI_note_taking
```

> **Step 3** Update the ```.env``` file

1) Create an OpenAI account from their OpenAI's [website](https://openai.com/). Verify and log in to the account and navigate to the API section. Here you can create a new API key. If in doubt, refer to [this thourough guide](https://www.maisieai.com/help/how-to-get-an-openai-api-key-for-chatgpt).

2) In order to use chatGPT API you need to pay a very small amount each time (around 0.05$ each time you run the script). This means, that your OpenAI account needs to have some funds in it.

3) Enter your ```OpenAI API key``` in the environment file ```.env```.

```bash
OPENAI_API_KEY = 'your-key-here'
```
4) Save the file. These are now global environment variables which the script can read when you run it.

> **Step 4** Run ```setup.sh```

To replicate the results, I have included a bash script that automatically 

1. Creates a virtual environment for the project
2. Activates the virtual environment
3. Installs the correct versions of the packages required
4. Runs the script
5. Deactivates the virtual environment

Run the code below in your bash terminal:

```bash
bash setup.sh
```

## Arguments 📜
You can change the Whisper model either manually in the ```function.py``` or via the terminal as an argument. Default is ```small```. This is how you would change model in via the terminal:
```
bash setup.sh --model_name medium
```
### Available models:
|  Size  | Parameters | English-only model | Multilingual model | Required VRAM | Relative speed |
|:------:|:----------:|:------------------:|:------------------:|:-------------:|:--------------:|
|  tiny  |    39 M    |     `tiny.en`      |       `tiny`       |     ~1 GB     |      ~32x      |
|  base  |    74 M    |     `base.en`      |       `base`       |     ~1 GB     |      ~16x      |
| small  |   244 M    |     `small.en`     |      `small`       |     ~2 GB     |      ~6x       |
| medium |   769 M    |    `medium.en`     |      `medium`      |     ~5 GB     |      ~2x       |
| large  |   1550 M   |        N/A         |      `large`       |    ~10 GB     |       1x       |


## Note 📒

Ensure you have the required API keys for OpenAI set up and that you are following OpenAI's terms of use while using these functions (ty chatgpt)

Please refer to OpenAI's [documentation](https://beta.openai.com/docs/) for more details on API usage and rate limits.

Feel free to explore and modify these functions to suit your specific text processing needs!

$$$$$$$$$$$$$$$$$$$$$$$$$$
Beware that using the OpenAI API is not free. It costs around 0.05$ each time you run the script on a 8000token text.
$$$$$$$$$$$$$$$$$$$$$$$$$$