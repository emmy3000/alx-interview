#!/usr/bin/node
const util = require('util');
const request = util.promisify(require('request'));

async function getFilmCharacters(filmId) {
  const filmUrl = `https://swapi-api.hbtn.io/api/films/${filmId}`;
  
  try {
    const response = await request(filmUrl);
    const film = JSON.parse(response.body);
    
    for (const characterUrl of film.characters) {
      const characterResponse = await request(characterUrl);
      const character = JSON.parse(characterResponse.body);
      console.log(character.name);
    }
  } catch (error) {
    console.error(`Error fetching data: ${error.message}`);
  }
}

const filmID = process.argv[2];
getFilmCharacters(filmID);
