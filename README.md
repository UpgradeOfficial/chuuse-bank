<div id="top"></div>

[![Contributors][contributors-shield]][contributors-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <!-- <a href="https://github.com/UpgradeOfficial/chuuse-bank">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a> -->

  <h3 align="center">CHUUSE BANK</h3>

  <p align="center">
    A SIMPLE BANK SOFTWARE
    <br />
    <a href="https://github.com/UpgradeOfficial/chuuse-bank"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://chuusebank.pythonanywhere.com/swagger/">View Demo</a>
    ·
    <a href="https://github.com/UpgradeOfficial/chuuse-bank/issues">Report Bug</a>
    ·
    <a href="https://github.com/UpgradeOfficial/chuuse-bank/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
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

[![Product Name Screen Shot][product-screenshot]](https://chuusebank.pythonanywhere.com/swagger/)

This is an open source project on building a simple banking software. Open source is very important and I am happy to support anything open source.

Here's why:

- FLEXIBILITY AND AGILITY
- SPEED
- COST-EFFECTIVENESS
- ABILITY TO START SMALL
- SOLID INFORMATION SECURITY
- ATTRACT BETTER TALENT
- SHARE MAINTENANCE COSTS
- THE FUTURE

Of course, no one single project  will serve all case since your needs may be different. So I'll be adding more in the near future(and your help will be greatly appreciated). You may also suggest changes by forking this repo and creating a pull request or opening an issue. Thanks to all the people who will contributed to expanding this Project!


<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

This project was built with the following technologies( as of the time of the last update of this readme file).

- [django](https://docs.djangoproject.com/en/4.0/)
- [django-rest](https://www.django-rest-framework.org/)
- [jwt](https://jwt.io/)
- [swagger](https://swagger.io/)




<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

Below is how to get started with this project.
<div>
## Requirements

See the requirements for this project [click here](https://github.com/UpgradeOfficial/chuuse-bank/blob/main/requirements.txt).

## Installation

- First clone the project into your local machine.

```bash
git clone https://github.com/UpgradeOfficial/chuuse-bank.git
```

- Go to the repository and create a virtual environment.

```bash
cd chuuse-bank
python3 -m venv venv
```

- Activate the virtual environment and install dependencies.

```bash
source venv/bin/activate
pip install -r requirements.txt
```

- Then install wheel, build-essential, python3-dev and psycopg2

```bash
pip install wheel
sudo apt install build-essential
sudo apt install python3-dev
pip install psycopg2
```

- Copy the `example.env` file to `.env` and fill in the values.

```bash
cp example.env .env
```

- The `.env` file should look like this:

```text
SECRET_KEY=your_secret_key
JWT_SECRET_KEY=your_jwt_secret_key
```

- Create and migrate the database.

```bash
python manage.py migrate
```

## Running the server

- You can run the server with the following command:

```bash
python manage.py runserver
```

- You can also run the server on a custom port by adding the port number after the `runserver` command:

```bash
python manage.py runserver 8000
```
</div>


<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ROADMAP -->

## Roadmap

- [x] Project Structure
- [x] Token Authentication
- [x] Add Test
- [ ] Add Email Functionality
- [ ] Add background jobs
  

See the [open issues](https://github.com/UpgradeOfficial/chuuse-bank/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

deye - [@IncreaseOdeyemi](https://twitter.com/IncreaseOdeyemi) - odeyemiincrease@yahoo.com

Project Link: [https://github.com/UpgradeOfficial/chuuse-bank](https://github.com/UpgradeOfficial/chuuse-bank)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->

## Acknowledgments

Special acknolegment to the following people/company/organisation:

- [Odeyemi Increase Ayobami](https://github.com/UpgradeOfficial/)
- [chuuse](https://trychuuse.com/)



<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/badge/Contributors-1-orange
[contributors-url]: https://github.com/UpgradeOfficial/chuuse-bank/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/UpgradeOfficial/chuuse-bank.svg?style=for-the-badge
[forks-url]: https://github.com/UpgradeOfficial/chuuse-bank/network/members
[stars-shield]: https://img.shields.io/github/stars/UpgradeOfficial/chuuse-bank.svg?style=for-the-badge
[stars-url]: https://github.com/UpgradeOfficial/chuuse-bank/stargazers
[issues-shield]: https://img.shields.io/github/issues/UpgradeOfficial/chuuse-bank.svg?style=for-the-badge
[issues-url]: https://github.com/UpgradeOfficial/chuuse-bank/issues
[license-shield]: https://img.shields.io/github/license/UpgradeOfficial/chuuse-bank.svg?style=for-the-badge
[license-url]: https://github.com/UpgradeOfficial/chuuse-bank/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/odeyemi-increase/
[product-screenshot]: media/github_images/project_preview.png
