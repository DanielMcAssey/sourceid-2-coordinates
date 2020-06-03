{
    'targets': [{
        'target_name': 'sourceid-2-coordinates',
        'include_dirs': [
            "<!(node -e \"require('nan')\")"
        ],

        'cflags': [
            '-Wall',
            '-Wparentheses',
            '-Winline',
            '-Wbad-function-cast',
            '-Wdisabled-optimization'
        ],

        'conditions': [
            ["OS=='win'", {
                'defines': ['IS_WINDOWS']
            }]
        ],

        'sources': [
            'src/index.cc',
            'src/sourceId2Coordinates.cc'
        ]
    }],

    'variables': {
        'build_v8_with_gn': 0
    },
}
