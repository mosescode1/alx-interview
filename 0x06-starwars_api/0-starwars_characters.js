#!/usr/bin/node
//"""Making request in node"""
const request = require("request");

const BASE_URL = "https://swapi-api.alx-tools.com/api/";

const movieId = +process.argv[2];

request(`${BASE_URL}films/${movieId}`, (err, response, body) => {
	if (err) {
		console.log(err);
	}
	const characters = JSON.parse(body).characters;
	const name = characters.map(
		lnk => new Promise((resolve, reject) => {
			request(lnk, (err, response, body) => {
				if (err) {
					reject(err);
				}
				const info = JSON.parse(body);
				resolve(info.name);
			});
		}));
	Promise.all(name)
		.then(names => console.log(names.join('\n')))
		.catch(x => console.log(err));
});