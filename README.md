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
- Notion
  ```
  Read the Notion Docs on how to obtain a NOTION TOKEN
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/chentze02/leetcode-notion-tracker.git
   ```
2. Enter your DATABASE KEY and NOTION TOKEN in the MACROS
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

Your Name - [@twitter_handle](https://twitter.com/twitter_handle) -
email@email_client.com

Project Link:
[https://github.com/github_username/repo_name](https://github.com/github_username/repo_name)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Disclaimer

This script is not affiliated with LeetCode or Notion. It is an independent tool
developed to enhance the tracking of LeetCode question progress using Notion.

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/chentze02/leetcode-notion-tracker/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/chentze02/leetcode-notion-tracker/
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com
