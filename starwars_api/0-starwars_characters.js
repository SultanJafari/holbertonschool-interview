
#!/usr/bin/node
const request = require('request');

const getData = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
};

const main = async () => {
  const movieId = process.argv[2];
  const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

  try {
    const movie = await getData(url);

    for (const characterUrl of movie.characters) {
      const character = await getData(characterUrl);
      console.log(character.name);
    }
  } catch (error) {
    console.error(error);
  }
};

main();
