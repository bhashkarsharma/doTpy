import re

class DoT:

    version = "1.0.3"
    
    templateSettings = {
			'evaluate' :    re.compile(r"\{\{([\s\S]+?(\}?)+)\}\}"),
			'interpolate' : re.compile(r"\{\{=([\s\S]+?)\}\}"),
			'encode' :      re.compile(r"\{\{!([\s\S]+?)\}\}"),
			'use' :         re.compile(r"\{\{#([\s\S]+?)\}\}"),
			'useParams' :   re.compile(r"(^|[^\w$])defi(?:\.|\[[\'\"])([\w$\.]+)(?:[\'\"]\])?\s*\:\s*([\w$\.]+|\"[^\"]+\"|\'[^\']+\'|\{[^\}]+\})"),
			'define' :      re.compile(r"\{\{##\s*([\w\.$]+)\s*(\:|=)([\s\S]+?)#\}\}"),
			'defineParams' :re.compile(r"^\s*([\w$]+):([\s\S]+)"),
			'conditional' : re.compile(r"\{\{\?(\?)?\s*([\s\S]*?)\s*\}\}"),
			'iterate' :     re.compile(r"\{\{~\s*(?:\}\}|([\s\S]+?)\s*\:\s*([\w$]+)\s*(?:\:\s*([\w$]+))?\s*\}\})"),
			'varname' :	'it',
			'strip' :		True,
			'append' :		True,
			'selfcontained' : False,
			'doNotSkipEncoded' : False
    }

    template = None # fn, compile template

    compile = None # fn, for express

    log = True

    @staticmethod
    def encodeHTMLSource(doNotSkipEncoded):
        encodeHTMLRules = { 
            "&": "&#38;", 
            "<": "&#60;", 
            ">": "&#62;", 
            '"': "&#34;", 
            "'": "&#39;", 
            "/": "&#47;" 
        }
        matchHTML = re.compile(r"[&<>\"'\/]") if doNotSkipEncoded else re.compile(r"&(?!#?\w+;)|<|>|\"|'|\/")

        def func(code):
            if not code:
                return ""
            scode = str(code)
            matches = re.findall(matchHTML, scode)
            for m in matches:
                f = re.sub(matchHTML, encodeHTMLRules.get(s, s), scode)
            return f
        
        return func
    
    startend = {
		'append': { 
            'start': "'+(",
            'end': ")+'",
            'startencode': "'+encodeHTML(" 
        },
		'split': { 
            'start': "';out+=(", 
            'end': ");out+='", 
            'startencode': "';out+=encodeHTML(" 
        }
	}
    
    skip = re.compile(r"$^")

    @staticmethod
    def resolveDefs(c, block, defi):
        if type(block) == str:
            return block
        sblock = str(block)
        
        def fun1(m, code, assign, value):
            pass
        
        def fun2(m, code):
            pass
        
        return re.sub(c.define or skip, fun1, sblock).sub(c.use or skip, fun2, )
    
    @staticmethod
    def unescape(code):
        pass
    
    @staticmethod
    def template(tmpl, c, defi):
        pass
    
    @staticmethod
    def compile(tmpl, defi):
        return template(tmpl, None, defi)
