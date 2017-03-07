# weather-tracker
Django Web App. Tracks weather for cities followed by the user.

This repo contains two Docker Compose configurations.
"docker-compose.first.dev.yml" will run data migrations, install fixtures, and import weather data from Open Weather maps.
"docker-compose.dev.yml" will simply start the service and run the django development server.

To start the service the first time: [sudo] docker-compose -f docker-compose.first.dev.yml up

Note that the Django web service is not failsafe, so if the database service does not launch before the Django service launches, the migrations and fixtures commands will fail. If this happens simply run the above command again.

To start the service after the first time: [sudo] docker-compose -f docker-compose.dev.yml up

To update the weather data, simply re-run either of the above docker-compose commands.
