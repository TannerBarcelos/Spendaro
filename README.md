# Spendaro

![Marketing Site Deployment](https://github.com/TannerBarcelos/Spendaro/actions/workflows/deploy-site.yaml/badge.svg)

**Helping make finance easier for everyone**

![Spendaro](./spendaro.png)

## About The Project

Spendaro is a personal finance application that helps you track your spending and budgeting. It is built with a modern tech stack and is designed to be easy to use. It is currently under development and is not ready for production use and a feature list is still being developed.

### Tech Stack

- **Frontend**

  - React (with Typescript)
  - Tailwind / Radix
  - Zustand for Client Side state management
  - Vitest for unit testing
  - Cypress for E2E tests

- **Backend**

  - Express
  - MySQL on Planetscale
  - DrizzleORM
  - Redis on Upstash
  - Jest for Unit and Integration Testing

- **Infrastructure**

  - Docker for containerization / compose for production _(Kubernetes is overkill for this project usecase right now)_
  - Ansible for deployment automation and configuration
  - Terraform for Linode VM provisioning automation 
  - Github Actions for CI/CD pipelines of each service in the monorepo

- **Project Management**
  - Figma for design
  - Github Projects for project management

## Features

Under development

## Getting Started

Please refer to the [contributing guide](./CONTRIBUTING.md) for information on how to get started with the project and how to contribute.
