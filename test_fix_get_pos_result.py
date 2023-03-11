from fix_get_pos_result import handle_single_arg

tests = [
    { 
        'input': "setpos -800.009644 -2879.966309 239.025986;setang -23.661070 114.181854 0.000000", 
        'ex': "setpos -800.009644 -2879.966309 174.963425;setang -23.661070 114.181854 0.000000"
    }
]

for test in tests:
    result = handle_single_arg(test['input'])
    assert result == test['ex'], 'expected: ' + test['ex'] + ' but was: ' + result