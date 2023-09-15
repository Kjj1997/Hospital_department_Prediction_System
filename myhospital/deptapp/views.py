import joblib
import os
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .forms import VisitReasonForm
from .models import VisitReason
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the pre-trained model
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR,'dept_pred.pkl')
model = joblib.load(model_path)

# Load the pre-trained TF-IDF vectorizer
tfidf_vectorizer_path = os.path.join(BASE_DIR,'rovvec.pkl')
tfidf_vectorizer = joblib.load(tfidf_vectorizer_path)

# Define the prediction function
def predict_department(encoded_text):
    predicted_department = model.predict([encoded_text])[0]
    return predicted_department

# Define the view for predicting department from a form submission
def visit_reason(request):
    if request.method == 'POST':
        form = VisitReasonForm(request.POST)
        if form.is_valid():
            # Get the user's input from the form
            reason_text = form.cleaned_data['reason_text']

            # Encode the reason_text using the TF-IDF vectorizer
            encoded_text = preprocess_and_encode_text(reason_text)

            # Get predictions
            predicted_department = predict_department(encoded_text)

            # Return the prediction as a response
            return HttpResponse(f'Predicted Department: {predicted_department}')
    else:
        form = VisitReasonForm()
    return render(request, 'deptapp/visit_reason.html', {'form': form})

# Helper function to preprocess and encode text
def preprocess_and_encode_text(text):
    encoded_text = tfidf_vectorizer.transform([text])
    # Convert the sparse matrix to an array
    encoded_text_array = encoded_text.toarray()
    return encoded_text_array[0]  # Return the first row as the encoded text

# Define the view for the homepage
def home(request):
    # Your view logic here
    return render(request, 'deptapp/home.html')



from rest_framework import viewsets

from .serializers import VisitReasonSerializer
from .models import VisitReason

class VisitReasonViewSet(viewsets.ModelViewSet):
    queryset = VisitReason.objects.all()
    serializer_class = VisitReasonSerializer



from django.shortcuts import redirect
def home_redirect(request):
    return redirect('home')


#API for department prediction based on the reason of visit given in url
def predict_department_api(request,reason_text):
    encoded_text = preprocess_and_encode_text(reason_text)
    probable_department = predict_department(encoded_text)

    return JsonResponse({'predicted_department':probable_department})