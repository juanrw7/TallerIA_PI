import os

from django.core.management.base import BaseCommand
from movie.models import Movie


class Command(BaseCommand):
    help = "Update movie images in the database from local image files"

    def handle(self, *args, **kwargs):
        images_folder = "media/movie/images"

        movies = Movie.objects.all()
        self.stdout.write(f"Found {movies.count()} movies")

        updated_count = 0

        for movie in movies:
            image_filename = f"m_{movie.title}.png"
            image_full_path = os.path.join(images_folder, image_filename)

            if os.path.exists(image_full_path):
                movie.image = os.path.join(
                    "movie/images",
                    image_filename
                )
                movie.save()

                updated_count += 1

                self.stdout.write(
                    self.style.SUCCESS(
                        f"Updated image for: {movie.title}"
                    )
                )
            else:
                self.stderr.write(
                    f"Image not found for: {movie.title}"
                )

        self.stdout.write(
            self.style.SUCCESS(
                f"Finished updating {updated_count} movie images."
            )
        )