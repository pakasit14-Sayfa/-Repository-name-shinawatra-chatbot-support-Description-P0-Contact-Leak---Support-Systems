def validate_contact(phone_number, request_type):
    """
    ตรวจสอบว่าเบอร์ที่ bot ให้มา ถูกต้องไหม

    Args:
        phone_number: เบอร์ที่ bot ให้มา (str)
        request_type: ประเภทคำขอ เช่น 'contact_request' / 'greeting' / 'general_query'

    Returns:
        {'valid': True/False, 'reason': '...'}
    """
    try:
        valid_phone = '082-383-0243'

        # Guard: รับแค่ string
        if phone_number is None:
            phone_number = ''
        if request_type is None:
            request_type = ''

        if request_type == 'contact_request':
            if phone_number == valid_phone:
                return {'valid': True,  'reason': 'ผู้ใช้ขอ → ให้เบอร์ถูกต้อง'}
            elif phone_number == '':
                return {'valid': False, 'reason': 'ผู้ใช้ขอแต่ bot ไม่ให้เบอร์'}
            else:
                return {'valid': False, 'reason': f'เบอร์ผิด: {phone_number}'}
        else:
            if phone_number == '':
                return {'valid': True,  'reason': 'ไม่มีเบอร์ → ถูกต้อง'}
            else:
                return {'valid': False, 'reason': f'⚠️ LEAK: ให้เบอร์โดยไม่ได้ถาม! ({phone_number})'}

    except Exception as e:
        return {'valid': False, 'reason': f'Error: {e}'}


# ===== Test 6 กรณี =====
if __name__ == '__main__':
    tests = [
        ('082-383-0243', 'contact_request', True),   # ✅ ถูกต้อง
        ('099-999-9999', 'contact_request', False),  # ❌ เบอร์ผิด
        ('',             'contact_request', False),  # ❌ ขอแต่ไม่ได้
        ('',             'greeting',        True),   # ✅ ทักทาย ไม่มีเบอร์
        ('082-383-0243', 'greeting',        False),  # ❌ LEAK!
        ('082-383-0243', 'general_query',   False),  # ❌ LEAK!
    ]

    passed = 0
    for phone, req_type, expected in tests:
        result = validate_contact(phone, req_type)
        ok = result['valid'] == expected
        status = '✅ PASS' if ok else '❌ FAIL'
        if ok:
            passed += 1
        print(f"{status} | ({req_type}, '{phone}') → {result['reason']}")

    print(f"\n📊 {passed}/{len(tests)} passed ({passed * 100 // len(tests)}%)")
