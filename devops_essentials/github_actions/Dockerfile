# Usar una imagen base oficial de Node.js
FROM node:14

# Crear y establecer el directorio de trabajo
WORKDIR /app

# Copiar package.json y package-lock.json
COPY package*.json ./

# Instalar las dependencias
RUN npm install

# Copiar el resto del código de la aplicación
COPY . .

# Exponer el puerto que la aplicación utilizará
EXPOSE 8080

# Comando para ejecutar la aplicación
CMD ["node", "app.js"]
