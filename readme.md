> Dynamically translate text between thousands of language pairs

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Frightlag%2F21-translator.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2Frightlag%2F21-translator?ref=badge_shield)

## Prerequisites

Install 21 Beta:

	$ curl https://21.co | sh

Create a [21 account](https://21.co/signup/).

## Usage

	$ 21 buy "jasonwalsh/21-translator/?q=the quick brown fox jumped over the lazy dog&target=es" -o out
	$ cat out

> "El zorro marrón rápido saltó sobre el perro perezoso"

:bangbang: **Note:** Unfortunately, the `-o` flag is **required** for this operation. If the flag is not specified, the output of the request contains escaped `UTF-8` text.

<p align="center">
  <img src="https://user-images.githubusercontent.com/2184329/29497208-f5f188b0-85b1-11e7-81aa-37d12d9d78b6.png" width="600">
</p>

## Query Parameters

| Parameter | Description                                                                                                                                                                                                                                                                                       |         Required         |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------:|
| `q`       | The input text to translate. Repeat this parameter to perform, translation operations on multiple text inputs.                                                                                                                                                                                    |    :heavy_check_mark:    |
| `target`  | The language to use for translation of the input text, set, to one of the language codes listed in [Language Support](https://cloud.google.com/translate/docs/languages).                                                                                                                         |    :heavy_check_mark:    |
| `format`  | The format of the source text, in either HTML (default) or, plain-text. A value of html indicates HTML and a value of text indicates, plain-text.                                                                                                                                                 | :heavy_multiplication_x: |
| `source`  | The language of the source text, set to one of the language, codes listed in [Language Support](https://cloud.google.com/translate/docs/languages). If the source language is not specified, the API will attempt to detect, the source language automatically and return it within the response. | :heavy_multiplication_x: |
| `model`   | The translation model. Can be either base to use the Phrase-Based, Machine Translation (PBMT) model, or nmt to use the Neural Machine Translation, (NMT) model. If omitted, then nmt is used.                                                                                                     | :heavy_multiplication_x: |

## License

[Jason Walsh](https://twitter.com/rightlag) &copy; [MIT](LICENSE)


[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Frightlag%2F21-translator.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Frightlag%2F21-translator?ref=badge_large)