ARG NODE_VERSION_TAG=20.5.1-slim
ARG EXPOSE_PORT=5173
ARG NODE_ENV

# Base Stage - Used for both dev and prod
FROM node:${NODE_VERSION_TAG} AS base
WORKDIR /usr/app
COPY package*.json ./
RUN npm install
COPY ./ ./

# Dev Stage - Used for development
FROM base AS dev
EXPOSE ${EXPOSE_PORT}
CMD ["npm", "run", "dev"]

# Base Prod Stage - Used for production pre-build for optimization
FROM base AS prod-base
RUN npm run build

# Prod Stage - Used for production
FROM node:${NODE_VERSION_TAG} AS prod
WORKDIR /usr/app
RUN ls -la
COPY --from=prod-base ./client/dist ./
CMD ["node", "dist/src/app.js"]
