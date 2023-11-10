# Use an official Node runtime as a parent image
FROM node:16-alpine

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json (if available)
COPY package*.json ./

# Install dependencies
RUN npm ci

# Copy the rest of your app's source code
COPY . .

# Your server runs on port 3000
EXPOSE 3000

# Define the command to start your app
CMD ["npm", "run", "dev"]
# CMD ["node", "app.js"]
