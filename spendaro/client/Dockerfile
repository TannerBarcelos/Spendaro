ARG NODE_VERSION_TAG=20.5.1-slim
ARG EXPOSE_PORT=5173
ARG NODE_ENV

###############
# Development #
###############
FROM node:${NODE_VERSION_TAG}
WORKDIR /usr/app
COPY package*.json ./
RUN npm install
COPY ./ ./
EXPOSE ${EXPOSE_PORT}
CMD ["npm", "run", "dev"]

##############
# Production #
##############
# Base Prod Stage
FROM node:${NODE_VERSION_TAG} AS prod-base
WORKDIR /usr/app
COPY package*.json ./
RUN npm install
COPY ./ ./
RUN npm run build

# Prod Stage (since the built application are static files, we can use nginx to serve them given Vite is not a production server and we need to serve the files!)
FROM nginx:1.19.10-alpine AS prod
WORKDIR /usr/app
COPY --from=prod-base /usr/app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
