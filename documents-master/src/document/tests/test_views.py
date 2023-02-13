from django.urls import reverse
from document.models import Document


def test_archive_document(document, admin_client):
    response = admin_client.post(reverse('gen_document:gen_document-archives', kwargs={'pk': str(document.id)}), data={})
    document_db = Document.objects.get(id=document.id)
    assert response.status_code == 200
    assert document.is_archive != document_db.is_archive
