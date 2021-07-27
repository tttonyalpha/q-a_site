from django import forms


class CreateNewQuestion(forms.Form):
    title = forms.CharField(max_length=150)
    text = forms.CharField(max_length=150)
    rating = forms.IntegerField()
    #added_at = forms.DateTimeField(auto_now_add=True)
    #author = models.ForeignKey(User, related_name="question_author", on_delete=models.CASCADE)
    #likes = models.ManyToManyField(User, related_name='question_like_user')
    #objects = QuestionManager()
