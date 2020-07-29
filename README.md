# Nuxt-fastapi-poc

Nuxt.js powered by FastAPI(with OpenAPI generator) as the backend server 

## includes:
* jest
* storybook
* eslint
* prettier

## Build Setup

``` bash
# install dependencies
$ yarn install

# serve with hot reload at localhost:3000
$ yarn dev

# build for production and launch server
$ yarn build
$ yarn start

# generate static project
$ yarn generate
```

For detailed explanation on how things work, check out [Nuxt.js docs](https://nuxtjs.org).

## OpenAPI Demo

```
yarn start:backend
yarn generate:openapi
```

Above will output endpoints of the Backend server as a method.
See [src/pages/inspire.vue](./src/pages/inspire.vue) for invocation. 
