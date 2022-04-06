class Country(models.Model):
    title = models.CharField(max_length=20)
    strength = models.IntegerField('Численность')

    def __str__(self):
        return self.title


class Club(models.Model):
    title = models.CharField(max_length=20)
    bulk_arena = models.IntegerField('Вместимость арены')
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Fun(models.Model):
    name = models.CharField(max_length=15)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# составить запрос:
# Список стран, аннотированный полем


# - количество фанатов, которые болеют за клубы, у которых вместимость арены больше 50к
Country.objects.filter(club__bulk_arena__gt=50).annotate(total=Count('club__fun'))


# - количество команд, за которых болеет более 3 человек
sub = Club.objects.filter(country=OuterRef('pk')).annotate(t=Count('fun')).filter(t__gt=3).annotate(l=Count('title', distinct=True)).values('l')
Country.objects.annotate(r=Subquery(sub))

# - количество фанатов, которые болеют за клуб с самым длинным названием


#
