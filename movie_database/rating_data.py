def rating_data(apps, schema_editor):
    Rating = apps.get_model("movies", "Rating")
    Movie = apps.get_model("movies", "Movie")
    Rater = apps.get_model("movies", "Rater")

    with open("u.data") as infile:
        csv_item = csv.reader(infile, delimiter='\t')

    # movie_id = Movie.objects.create([0])
    # rater_id = Rater.objects.create([0])

        for row in csv_item:
            Rating.objects.create(user_id=row[0], item_id=row[1], rating=row[2], timestamp=row[3],
                                  movie_id=Movie.objects.create([0]), rater_id=Rater.objects.create([0]))

    raise Exception("Rating yay!")

