import cezar
import diffie_hellman

def test_cezar_encrypt_decrypt():
    # Проверяем, что зашифрованный и затем расшифрованный текст совпадает с оригиналом
    original_text = "hello test message"
    key = 5
    encrypted = cezar.encrypt(key, original_text)
    decrypted = cezar.decrypt(key, encrypted)
    assert decrypted == original_text

def test_cezar_without_key():
    # Создаем строку, где пробел — самый частый символ, как того требует ваша логика
    original_text = "test text with many spaces to check logic"
    key = 7
    encrypted = cezar.encrypt(key, original_text)
    # Проверяем взлом Цезаря без ключа
    decrypted = cezar.decrypt_without_key(encrypted)
    assert decrypted == original_text

def test_vernam():
    # Проверяем шифр Вернама. Ключ строго 8 символов.
    res = cezar.vernam('00001111', 'test')
    assert 'test -->' in res  # Проверяем ожидаемый формат вывода

def test_diffie_hellman_math():
    # Проверяем генерацию и совпадение ключей Диффи-Хеллмана
    a = 10
    b = 3478
    g = 634
    p = 6589
    
    A = diffie_hellman.client_key_send(a, g, p)
    B = diffie_hellman.server_key_send_receive(b, g, p, A)
    
    # Формулы вычисления итогового общего ключа
    K_a = (B**a) % p
    K_b = (A**b) % p
    
    # Главное правило Диффи-Хеллмана: итоговые ключи должны совпасть
    assert K_a == K_b
