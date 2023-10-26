import axios from "axios";
const cheerio = require("cheerio");

export const Crawl = async function (url) {
    const response = await axios.get(url)
    const $ = cheerio.load(response.data)
    console.log($)
}
