import csv


def movie_data(apps, schema_editor):
    Movie = apps.get_model("movies", "Movie")

    with open("u.item", encoding="latin1") as infile:
        csv_item = csv.reader(infile, delimiter='|')

        for row in csv_item:
            Movie.objects.create(movie_id=row[0], movie_title=row[1], release_date=row[2], video_release_date=row[3],
                                 IMDb_URL=row[4], unknown=row[5], action=row[6], adventure=row[7], animation=row[8],
                                 childrens=row[9], comedy=row[10], crime=row[11], documentary=row[12], drama=row[13],
                                 fantasy=row[14], film_noir=row[15], horror=row[16], musical=row[17], mystery=row[18],
                                 romance=row[19], sci_fi=row[20], thriller=row[21], war=row[22], western=row[23])

    # raise Exception("Movie yay!")


def rater_data(apps, schema_editor):
    Rater = apps.get_model("movies", "Rater")

    with open("u.user") as infile:
        csv_item = csv.reader(infile, delimiter='|')

        for row in csv_item:
            Rater.objects.create(user_id=row[0], age=row[1], gender=row[2], occupation=row[3], zip_code=row[4])

    # raise Exception("Rater yay!")


def rating_data(apps, schema_editor):
    Rating = apps.get_model("movies", "Rating")
    Movie = apps.get_model("movies", "Movie")
    Rater = apps.get_model("movies", "Rater")

    with open("u.data") as infile:
        csv_item = csv.reader(infile, delimiter='\t')

    # movie_id = Movie.objects.create([0])
    # rater_id = Rater.objects.create([0])

        for row in csv_item:
            movie = Movie.objects.get(id=row[0])
            rater = Rater.objects.get(id=row[0])

            Rating.objects.create(user_id=row[0], item_id=row[1], rating=row[2], timestamp=row[3],
                                  movie_id=movie, rater_id=rater)

        # raise Exception("Rating yay!")
