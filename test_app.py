from app import app

def test_home_status_code():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

def test_cadastrar_ocorrencia():
    client = app.test_client()
    response = client.post('/cadastrar', data={
        'tipo': '⚠️ Movimentação Suspeita',
        'descricao': 'Teste automatizado de alerta'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'Teste automatizado de alerta' in response.data