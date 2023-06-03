<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->

<a name="readme-top"></a>

<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
            *** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">

<h3 align="center">LeetCode Notion Tracker</h3>

<p align="center">
    Quick way to keep track of problems you solved on Notion by running a python script
    <br />
    <br />
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

The LeetCode Notion Tracker is a Python script that allows you to easily track
your progress in solving LeetCode questions by integrating with Notion, a
popular productivity and note-taking tool. With this script, you can
conveniently add LeetCode questions to your Notion database and keep track of
the questions you have completed.

## Features

- **Question Tracking**: The script allows you to add LeetCode questions to your
  Notion database and update the status of completed questions.
- **Automatic Data Retrieval**: It retrieves question information from the
  LeetCode API, such as difficulty level and question title.
- **Notion Integration**: Utilizes the Notion API to create and update pages in
  your Notion database.
- **Command-Line Interface**: You can interact with the script through a
  command-line interface by providing the LeetCode question number as an
  argument.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

This is an example of how you may give instructions on setting up your project
locally. To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to
install them.

- Python
  ```sh
  Python 3.11
  ```
- EnvFile
  ```sh
  pip install python-dotenv
  ```
- Notion
  ```
  Read the Notion Docs on how to obtain a NOTION TOKEN
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/chentze02/leetcode-notion-tracker.git
   ```

2.Setup your token and database id

###### Option 1 (RECOMMENDED)

1. Install the `python-dotenv` package by running `pip install python-dotenv` in
   your terminal.

2. Create an environment file (e.g., `.env`) in the `/usr/local` directory and
   populate it with your sensitive information:

`NOTION_TOKEN=YOUR_NOTION_TOKEN DATABASE_ID=YOUR DATABASE ID`

Ensure that the environment file has the appropriate permissions set to protect
the sensitive data.

1. Update the script to load the environment variables from the file using
   `load_dotenv()` function from the `dotenv` module. Provide the path to your
   environment file as an argument to `load_dotenv()`.

Make sure to replace `/usr/local/.env` with the correct path to your environment
file.

###### Option 2

Enter your DATABASE KEY and NOTION TOKEN in the MACROS

```python
# TOKEN AND IDS
NOTION_TOKEN = "YOUR_NOTION_TOKEN" 
DATABASE_ID = "YOUR_DATABASE_ID"
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Make it a Bash Command

To set up the LeetCode Notion Tracker script as a bash command, follow these
steps:

1. Open a terminal.
2. Navigate to the directory where the script is located.
3. Rename the script file to `leetcode` without the `.py` extension.

   `mv leetcode-tracker.py leetcode`

4. Make the script executable.

   `chmod +x leetcode`

5. Move the script to the `/usr/local/bin` directory.

   `sudo mv leetcode /usr/local/bin/`

   You will be prompted to enter your password for the sudo command.
6. Verify the installation by running the command `leetcode <leetcode_number>`
   in the terminal. Replace `<leetcode_number>` with the actual LeetCode
   question number.

Now you can use the `leetcode` command as if it was a built-in bash command.

<!-- USAGE EXAMPLES -->

## Usage

To add or update a LeetCode question in your Notion database, follow these
steps:

1. Open a terminal or command prompt.
2. Navigate to the directory where the script is located.
3. Run the script using the command `python your_script.py <leetcode_number>`,
   replacing `<leetcode_number>` with the actual question number.
4. The script will fetch the question details from the LeetCode API and check if
   the question already exists in your Notion database.
5. If the question exists, it will update the question's status with the current
   date and time.
6. If the question does not exist, it will create a new entry in your Notion
   database with the question details and set the status to the current date and
   time.

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to
learn, inspire, and create. Any contributions you make are **greatly
appreciated**.

If you have a suggestion that would make this better, please fork the repo and
create a pull request. You can also simply open an issue with the tag
"enhancement". Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

Your Name - chentzen02@g.ucla.edu

Project Link:
[https://github.com/github_username/repo_name](https://github.com/chentze02/leetcode-notion-tracker))

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Disclaimer

This script is not affiliated with LeetCode or Notion. It is an independent tool
developed to enhance the tracking of LeetCode question progress using Notion.

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->


[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/chentzen02/
[product-screenshot]: images/screenshot.png
