# 0x06. Star Wars API

## Overview

This script retrieves and prints the names of characters from a Star Wars movie based on the Movie ID provided as a command-line argument. It utilizes the Star Wars API and the request module in Node.js.

## Usage

**Prerequisites**

- Node.js installed on your machine.
```shell
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

- Install JavaScript Semi-Standard Style
```shell
npm install semistandard --global
```

### How to Run

1. Create & navigate to the project directory:

```shell
mkdir 0x06-star-wars-api
cd 0x06-star-wars-api
```

**Example**

2. Run the script with the Movie ID as a command-line argument:

```shell
./0-starwars_characters.js 3
```
- The integer value 3 equates to the movie title called "Return of the Jedi".

**OUTPUT**
- The command will output the names of characters from the movie with ID 3.
```shell
$ ./0-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
```

### Notes

1. Make sure you have an internet connection to access the Star Wars API.
2. The script uses the request module, so make sure to install the necessary dependencies if not already installed:
```shell
npm install request
```

## Author
Emeka Emodi
