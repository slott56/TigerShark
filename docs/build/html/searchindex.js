Search.setIndex({"docnames": ["architecture", "design/annotations", "design/classmodel", "design/element", "design/index", "design/loopmodel", "design/parsing", "implementation/index", "implementation/tools", "implementation/x12", "index", "operation", "overview", "todo", "usecase"], "filenames": ["architecture.rst", "design/annotations.rst", "design/classmodel.rst", "design/element.rst", "design/index.rst", "design/loopmodel.rst", "design/parsing.rst", "implementation/index.rst", "implementation/tools.rst", "implementation/x12.rst", "index.rst", "operation.rst", "overview.rst", "todo.rst", "usecase.rst"], "titles": ["Architecture and Design", "Type Hints", "Class Model", "Element Class Design", "Design Notes", "Loops as Namespaces", "Parsing An Exchange-Format Message", "Implementation", "<code class=\"docutils literal notranslate\"><span class=\"pre\">tools</span></code> Package", "<code class=\"docutils literal notranslate\"><span class=\"pre\">X12</span></code> Package", "Tiger Shark X12 Tools", "Using TigerShark", "Overview", "The TODO List", "Context: Use Cases"], "terms": {"thi": [0, 1, 2, 3, 5, 6, 8, 9, 11, 12, 13, 14], "document": [0, 3, 7, 8, 11, 13], "provid": [0, 1, 2, 3, 5, 6, 8, 9, 11, 12, 14], "an": [0, 1, 2, 3, 5, 8, 9, 11, 13], "overview": [0, 10, 14], "principl": 0, "The": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 14], "chapter": [0, 14], "describ": [0, 5, 8, 12, 14], "strategi": 6, "packag": [0, 4, 7, 10, 11, 12], "structur": [0, 1, 2, 5, 6, 9, 11, 12], "underli": 0, "softwar": [0, 4, 6, 12], "variou": [0, 2, 3, 5, 11, 12, 14], "kind": [0, 5, 6, 8], "occur": [0, 6], "contain": [1, 5, 6, 8, 10, 12, 14], "57": 0, "distinct": [0, 5, 8, 9, 14], "requir": [0, 1, 5, 6, 8, 11, 14], "us": [0, 1, 2, 3, 5, 6, 8, 9, 10, 12], "case": [0, 1, 2, 3, 8, 9, 10, 11], "There": [0, 1, 5, 6, 9, 11, 14], "ar": [0, 1, 2, 3, 4, 5, 6, 8, 9, 11, 14], "two": [0, 1, 3, 5, 6, 8, 9, 14], "view": [6, 10], "develop": 14, "s": [1, 2, 3, 5, 6, 8, 9, 11, 14], "It": [0, 1, 2, 3, 6, 8, 9, 11, 14], "class": [0, 1, 4, 8, 9, 10, 13, 14], "preliminari": [], "step": 0, "transform": 0, "format": [0, 3, 8, 9, 10, 12, 14], "plain": [0, 5, 11, 12], "old": [0, 5, 11, 12], "python": [0, 1, 2, 3, 5, 8, 10, 12, 14], "object": [0, 1, 2, 5, 8, 9, 11, 12, 13, 14], "popo": [0, 12], "A": [0, 1, 3, 5, 6, 8, 9, 11], "implement": [0, 1, 5, 8, 9, 10, 13, 14], "modul": [0, 2, 4, 8, 9, 10, 11, 14], "can": [0, 1, 3, 5, 6, 8, 9, 11, 12, 14], "import": [1, 2, 5, 6, 8, 9, 11, 14], "simplest": [], "standard": 0, "claim": [0, 12], "edi": [0, 1, 6, 8, 12, 14], "hipaa": [0, 1, 2], "have": [0, 1, 2, 3, 5, 6, 8, 9, 11, 14], "interchang": [0, 1, 2, 3, 8], "gatewai": [], "handl": [0, 9, 12], "tremend": [], "number": [0, 1, 3, 5, 6, 8, 9, 11], "individu": [1, 3, 9], "loop": [0, 2, 4, 6, 8, 9, 10, 11, 13, 14], "element": [0, 2, 4, 5, 6, 8, 9, 10, 11, 13, 14], "make": [0, 1, 3, 5, 8], "difficult": [0, 5], "creat": [0, 5, 8, 9, 10, 12, 13, 14], "meaning": 5, "manual": [6, 14], "defin": [0, 1, 2, 3, 5, 6, 7, 8, 9], "via": [0, 1], "sef": [0, 11], "file": [0, 5, 8, 11, 14], "addit": [0, 1, 3, 8, 11], "manag": 0, "complex": [0, 3], "sever": [0, 5, 8, 11], "layer": 8, "interpret": [0, 2], "exchang": [0, 5, 9, 10, 14], "big": 0, "block": 0, "rather": [], "sinc": 2, "must": [6, 8, 9], "rel": 0, "easi": [0, 6], "decompos": [0, 6, 9], "sequenc": [0, 1, 5, 6, 8, 9], "known": [], "pure": [1, 9, 13], "lexic": [6, 9], "analysi": [1, 14], "so": 9, "we": [0, 1, 3, 6, 9, 11, 12, 14], "call": 9, "token": [], "also": [0, 1, 2, 9, 14], "conveni": [], "form": [0, 3], "fix": 9, "see": [0, 1, 2, 6, 8, 12, 14], "closer": [], "mean": [0, 1, 6, 8, 9], "sourc": [0, 1, 3, 6, 9, 11, 13, 14], "semant": 12, "content": [2, 5], "determin": [], "given": [1, 8, 11, 13], "somewhat": [1, 2, 3], "more": [0, 1, 2, 5, 6, 8, 9, 11, 14], "flexibl": 11, "guid": [0, 14], "mai": [0, 1, 3, 8, 9], "alter": [], "situat": [1, 8], "Not": 8, "statu": 0, "elig": [0, 1, 2, 12, 14], "request": 0, "most": 9, "x12n": [], "necessari": [3, 6], "hand": [], "challeng": 8, "well": [1, 14], "vendor": [], "uniqu": [5, 6, 8], "complianc": 1, "check": 11, "ha": [0, 1, 2, 5, 6, 8, 9, 11, 14], "perform": [], "custom": 0, "code": [0, 1, 8, 9, 12, 13, 14], "each": [0, 2, 3, 5, 6, 8, 9, 11, 14], "payer": 0, "than": [5, 8], "write": [8, 11], "tigershark": [0, 1, 10, 12, 13, 14], "includ": [0, 1, 2, 3, 9, 11, 12], "tool": [0, 7, 9, 11, 12, 13, 14], "parser": 6, "set": [0, 1, 8, 9], "These": [0, 1, 3, 8, 14], "don": [1, 6], "t": [1, 2, 6, 8, 9], "complet": [0, 3, 8], "work": [0, 1, 6, 8, 11], "thei": [0, 1, 8, 14], "80": 0, "need": [3, 5, 9], "some": [0, 2, 5, 6, 8, 9, 11, 14], "tweak": [11, 14], "usual": [], "integr": [1, 8], "pars": [0, 1, 4, 8, 9, 10, 12, 14], "locat": [0, 2, 6, 8, 9, 13, 14], "within": [0, 1, 5, 6, 8, 14], "build": [0, 1, 5, 8, 9, 11, 14], "from": [0, 1, 2, 5, 6, 8, 9, 11, 13, 14], "quit": [], "simpl": [0, 6], "part": [0, 1, 3, 5, 8], "relat": [0, 8], "map": [13, 14], "three": [6, 9, 14], "pyx12": [0, 1, 8, 9, 11, 13, 14], "xml": [0, 1, 8, 11, 12, 14], "reason": [0, 1], "perl": [], "0": [1, 3, 8, 9, 14], "08": [], "cf": [], "which": [0, 2, 6, 8, 12, 14], "similar": [0, 6, 11, 14], "ini": [], "just": 6, "enough": [], "inform": [0, 1, 2, 3, 8, 9], "minim": 9, "publish": [], "disa": [], "oper": 0, "howev": [1, 3, 6, 11], "re": [3, 8, 13], "hard": [], "direct": [], "what": [0, 6], "collect": [0, 1, 8, 9], "truli": [], "univers": 0, "lead": [0, 3, 9, 14], "follow": [0, 2, 3, 4, 5, 6, 8, 9, 11, 14], "reli": [0, 1, 5, 9], "access": 0, "x12messag": [], "composit": [0, 2, 4, 5, 6, 8, 9, 11, 13, 14], "should": [0, 1, 3, 5, 6, 8, 13], "reflect": [0, 5], "wai": [3, 5, 8], "intepret": [], "impos": [], "least": 8, "mid": [], "user": 13, "orient": [], "e": [0, 8, 9, 14], "elgibl": [], "etc": [5, 8, 9, 14], "One": [], "list": [0, 1, 2, 3, 6, 8, 9, 10, 11], "segement": 0, "permit": [0, 6, 8, 11, 14], "veri": [1, 5], "limit": [0, 5], "chang": [3, 14], "made": [6, 8], "unknown": [], "easili": 1, "ad": [0, 1, 3, 11], "remov": 1, "extens": 8, "metadata": [], "That": [], "store": [], "identif": [0, 8, 13], "singl": [0, 1, 5, 9], "tabl": 0, "few": 6, "heavili": 8, "reus": [0, 1, 2, 3, 5, 8, 14], "x12loop": [], "x12segment": [], "instanc": [0, 1, 9, 14], "tie": [], "proper": 1, "allow": [0, 3], "load": [], "fk": [], "refer": [0, 1, 8], "all": [0, 5, 8, 9, 11], "understand": [], "particular": [], "x12element": [], "For": [0, 1, 2, 3, 5, 6, 9, 14], "exammpl": [], "find": [5, 6, 13], "posit": [1, 3, 6], "name": [0, 1, 2, 4, 9, 11, 14], "order": [0, 1, 8], "retriev": [], "final": [6, 8], "output": 1, "string": [0, 2, 3, 6, 8, 9, 11], "upsid": [], "trivial": 3, "independ": [], "ani": [0, 3, 8, 9], "specif": [0, 3, 6, 8, 9, 14], "downsid": [], "automat": [], "django": [], "admin": [], "page": 10, "won": [], "field": [6, 9, 11, 13], "possibl": [], "interact": [], "touch": 0, "up": [8, 9], "without": 3, "dynam": [], "larger": [], "origin": [0, 1, 13], "link": [], "larg": 0, "match": [8, 9], "howsev": [], "further": [1, 3, 14], "directli": 11, "g": [9, 14], "exampl": [1, 5, 6, 8, 9, 13, 14], "could": [0, 1, 3, 6, 8, 11], "bill": 0, "pai": 0, "To": [0, 3], "subscrib": 0, "patient": 0, "render": 0, "submitt": 0, "servic": [0, 1], "line": [0, 1, 6, 13], "adj": [], "attend": 0, "physician": 0, "highli": [], "while": [], "handi": [2, 12], "end": [0, 6], "fair": [], "amount": 0, "care": [0, 1, 2, 5], "translat": [], "between": [0, 3], "best": [11, 14], "approach": [3, 5, 6], "decis": [], "consequ": 6, "chose": [], "In": [1, 2, 3, 8, 9], "sql": [], "addition": 12, "appropri": [], "kei": 14, "valu": [0, 1, 2, 3, 6, 8, 9, 13, 14], "abov": [3, 13], "beyond": [], "variat": [], "slightli": [6, 14], "differ": [6, 14], "subclass": [1, 2, 8, 11, 13, 14], "descriptor": [], "db": [], "preclud": [], "other": [0, 2, 8, 9, 12, 14], "hierarchi": [0, 5], "being": 1, "explicit": 1, "sqlalchemi": [], "plu": [], "decor": [], "837": 12, "exhaust": [], "produc": [], "convers": [0, 2, 3, 9], "featur": [1, 3, 6, 9, 11, 13], "default": [6, 9], "impli": 3, "templat": 1, "factori": [], "plug": [], "support": [0, 3, 8], "one": [1, 6, 8, 14], "style": 9, "either": 9, "intend": [], "pattern": [], "outsid": 12, "here": [0, 1, 3, 6, 8, 9, 14], "illustr": [], "relationship": 6, "interfac": [], "web": [], "gui": [], "css": [], "extent": 3, "static": [], "media": [], "serv": [], "apach": [], "navig": 0, "built": [0, 1, 2, 11, 14], "url": [], "function": [0, 1, 2, 3, 8, 11], "domain": [], "callabl": [], "client": 9, "site": [], "instal": [], "wsgi": [], "enabl": [], "rpc": [], "rdbm": [], "core": 8, "those": 6, "both": 8, "tree": [8, 14], "place": [], "pythonpath": [], "librari": [], "essenti": 6, "depend": [2, 8, 10], "emit": [8, 10, 13], "util": [], "like": [1, 2, 3, 5, 8, 11], "extend": [], "seem": [0, 1, 2, 5, 6, 8, 9, 11], "convertpyx12": [], "convert": [0, 1, 3, 11], "surveypyx12": [], "get": [9, 11, 13], "when": [0, 1, 6, 9, 14], "project": [0, 1, 8, 11, 14], "would": [1, 2], "version": [0, 11, 13], "how": [0, 1, 14], "undividu": [], "involv": [], "modifi": [0, 1, 14], "download": [], "actual": 8, "declar": [5, 8], "itself": [], "global": [], "bookkeep": [], "identifi": [0, 1, 3, 6, 8, 14], "belong": [], "our": [], "goal": [], "leverag": 9, "pk": [], "whole": [8, 9], "attempt": [], "might": [3, 6, 8, 11, 13], "simpler": 3, "indent": 11, "outlin": [], "edit": [], "button": [], "similarli": 8, "option": [1, 3, 9], "repeat": [3, 8, 9, 14], "add": [], "placehold": [], "insert": [], "msg": [1, 9, 11, 14], "id": [0, 1, 2, 3, 8], "test": [0, 11, 14], "isa": [0, 1, 5, 6, 8, 9, 14], "gs": [0, 8], "st": [0, 6, 14], "bht": [0, 14], "header": [0, 1, 2, 9, 14], "2000a": [], "nm1": 0, "n3": [0, 8], "n4": [0, 1, 8], "hi": 0, "trailer": [0, 1, 3], "se": 0, "ge": [0, 8], "iea": [0, 1, 3, 5, 8, 9], "html": [], "manner": [], "common": [0, 1, 2, 3, 5, 6, 8], "scenario": 10, "organ": 0, "onc": [], "been": 1, "remain": [1, 6], "turn": 9, "lower": [], "collaps": [], "cooper": [], "method": [0, 1, 2, 6, 9, 11, 14], "recurs": 14, "descent": [], "assembl": [], "encod": 6, "show": [], "appli": [2, 8, 9], "top": [5, 9], "adequ": [], "combin": 14, "done": [], "parserbuild": [], "1": [1, 3, 6], "construct": [0, 8, 9], "constructor": [], "introspect": [], "2": [0, 1, 2, 3, 6, 8, 11], "sa": [], "seri": 1, "3": [1, 6], "becom": [3, 8, 9, 14], "live": [], "input": [], "merg": [], "simpli": [], "attribut": [0, 1, 2, 3, 8, 9, 11, 14], "entir": 9, "subtyp": [], "amt": 0, "estim": 0, "due": 0, "paid": 0, "sale": 0, "tax": 0, "coordin": 0, "benefit": 0, "cob": 0, "respons": 0, "total": 0, "medicar": 0, "deni": 0, "submit": 0, "charg": 0, "facil": 0, "discount": 0, "b": [0, 8], "trust": 0, "fund": 0, "postag": 0, "diagnost": 0, "group": [0, 1, 3, 14], "drg": 0, "outlier": 0, "cover": 0, "prior": 0, "payment": 0, "non": [0, 9, 11], "approv": 0, "per": 0, "dai": 0, "befor": [0, 11], "credit": 0, "debit": 0, "card": 0, "maximum": [0, 8], "100": [0, 8], "purchas": 0, "begin": 0, "hierarch": 0, "transact": [0, 8, 14], "ca": 0, "adjust": 0, "cl1": 0, "institut": 0, "clm": 0, "cn1": 0, "contract": 0, "cr1": 0, "ambul": 0, "transport": 0, "cr2": 0, "spinal": 0, "cr3": 0, "durabl": 0, "medic": [0, 1, 12], "equip": 0, "certif": 0, "cr5": 0, "home": 0, "oxygen": 0, "therapi": 0, "cr6": 0, "health": [0, 1, 2], "cr7": 0, "plan": 0, "crc": 0, "epsdt": 0, "referr": 0, "activ": 0, "dmerc": 0, "condit": [0, 8], "indic": 0, "homebound": 0, "hospic": 0, "employe": 0, "vision": 0, "mental": 0, "ctp": 0, "drug": 0, "price": 0, "cur": 0, "foreign": 0, "currenc": 0, "dmg": [0, 6], "demograph": 0, "insur": 0, "dn1": 0, "orthodont": 0, "month": 0, "treatment": 0, "dn2": 0, "tooth": 0, "dtp": 0, "date": [0, 3, 14], "onset": 0, "current": [0, 3, 5, 9], "symptom": 0, "ill": 0, "assess": 0, "adjud": 0, "last": [0, 6], "x": [0, 3], "rai": 0, "initi": [0, 9], "acut": 0, "manifest": 0, "menstrual": 0, "period": 0, "seen": 0, "disabl": 0, "applianc": 0, "placement": 0, "assum": 0, "relinquish": 0, "author": [0, 2], "return": [0, 9], "satur": 0, "arteri": 0, "blood": 0, "ga": 0, "ship": 0, "replac": [0, 8, 9, 13], "accid": 0, "discharg": 0, "revis": 0, "statement": 0, "admiss": 0, "hour": 0, "hear": 0, "prescript": 0, "frm": 0, "hcp": 0, "repric": 0, "diagnosi": 0, "occurr": 0, "span": 0, "princip": 0, "admit": 0, "visit": 0, "procedur": [0, 1], "hl": [0, 5, 14], "hsd": 0, "deliveri": 0, "control": [0, 1, 2, 3, 8], "k3": 0, "lin": 0, "lq": 0, "lx": 0, "counter": 0, "mea": 0, "result": [0, 12, 14], "mia": 0, "inpati": 0, "moa": 0, "outpati": 0, "address": 0, "destin": [0, 14], "parti": 0, "citi": 0, "state": [0, 3, 9], "zip": 0, "holder": 0, "receiv": 0, "assist": 0, "surgeon": 0, "supervis": 0, "account": 0, "nte": 0, "note": [0, 1, 2, 8, 9, 10, 14], "oi": 0, "coverag": 0, "pat": 0, "contact": 0, "prv": 0, "specialti": 0, "ps1": 0, "pwk": 0, "supplement": [0, 3], "cmn": 0, "qty": 0, "anesthesia": 0, "quantiti": 0, "ref": [0, 1, 8], "secondari": 0, "icn": 0, "dcn": 0, "item": [0, 1, 8], "mammographi": 0, "clearinghous": 0, "transmiss": 0, "intermediari": 0, "investig": 0, "devic": 0, "exempt": 0, "immun": 0, "batch": 0, "properti": [0, 1, 8, 9, 13], "casualti": 0, "demonstr": [0, 9], "clear": [0, 1, 3, 8], "hous": 0, "clinic": 0, "laboratori": 0, "improv": 0, "amend": 0, "clia": 0, "record": [0, 8], "mandatori": 0, "section": [0, 8, 14], "4081": 0, "crossov": 0, "peer": 0, "review": 0, "pro": 0, "ambulatori": 0, "apg": 0, "flow": 0, "rate": 0, "product": [0, 1], "upn": 0, "predetermin": 0, "except": [0, 9, 11], "sbr": 0, "sv1": 0, "profession": 0, "sv2": 0, "sv3": 0, "dental": 0, "sv5": 0, "svd": 0, "ta1": [0, 1], "acknowledg": 0, "too": 0, "architectur": [10, 14], "model": 10, "root": [], "persist": 0, "certain": [], "implicit": [], "rule": [8, 14], "associ": [], "attribiut": [], "defeat": 5, "ordinari": 0, "definit": [1, 2, 3, 4, 9, 10, 11, 12, 14], "techniqu": [], "inherit": [], "caus": [], "issu": 13, "repres": 1, "messag": [2, 3, 4, 5, 9, 10, 12, 13], "strongli": [], "type": [0, 2, 3, 4, 6, 9, 10, 13, 14], "switch": [], "loos": [], "gain": [], "consid": [8, 9, 13], "arbitrari": [], "constrain": [], "orm": [], "gener": [0, 1, 4, 8, 9, 11], "doesn": [2, 8], "databas": [], "save": [], "altern": [1, 5, 6, 11, 14], "instead": 1, "tightli": 1, "bound": [], "certainli": [], "bridg": [], "impact": [], "exist": [], "extern": 8, "rewrit": [], "x12": [1, 2, 3, 6, 7, 12, 13], "small": [0, 14], "tend": 5, "bind": [], "even": 11, "do": [9, 11, 13], "process": [1, 8, 10, 12, 14], "formal": [0, 1], "applic": [1, 8, 11, 14], "terribl": [], "assur": 0, "precis": [], "same": 8, "api": 7, "elimin": 3, "emul": [], "framework": [], "minor": [], "indirect": 1, "creation": 0, "onli": [0, 2, 8, 9, 13, 14], "where": [0, 3, 5, 6, 8, 9], "app": 8, "run": [0, 8, 11], "time": 3, "configur": 0, "want": [], "complic": [0, 1, 3, 5, 6, 8], "real": 3, "django_settings_modul": [], "environ": [], "variabl": [], "ideal": 11, "respect": [], "py": [0, 5, 11, 13], "correctli": [], "d": 3, "setup_environ": [], "ve": [], "Or": 3, "exec": [], "off": [], "stick": [], "sepecif": [], "represent": [0, 6, 11, 12], "reconcil": [], "among": [], "As": [], "read": [0, 6, 8, 9], "marshal": [], "unmarshal": [], "manipul": 0, "flat": [5, 9], "text": [0, 1, 2, 3, 5, 6, 8, 9, 13], "column": [], "summar": [], "multipl": [0, 2, 8, 9, 13], "moder": [], "natur": [], "look": [0, 1, 9, 11, 12, 14], "simplifi": 12, "program": [], "readili": [], "avail": [0, 3], "use": [], "first": [1, 3, 6, 8, 9], "segment": [0, 2, 3, 4, 5, 8, 9, 13, 14], "sometim": [6, 14], "separ": [1, 3, 6, 8, 9, 13], "basic": [], "fundament": [], "close": [], "synthes": [], "scratch": [], "intern": [1, 2, 3], "level": [0, 2, 5, 8, 9], "xpath": [], "queri": [], "through": [0, 2], "come": 1, "convertsef": [], "schema": [1, 2, 3, 4, 5, 9, 10, 12, 13, 14], "fold": [], "reusabl": [2, 8, 9], "effect": [], "push": [], "incomplet": [], "valid": [3, 13], "prevent": [], "logic": [], "less": 0, "transpar": [], "usabl": 0, "term": [], "If": [1, 6, 8], "present": [5, 6, 8], "i": 10, "tier": [], "mapp": [], "eligbl": [], "exclus": 8, "facad": [], "duplic": 8, "higher": 8, "friendli": 11, "busi": [], "focus": 3, "At": 8, "know": 6, "often": [0, 2, 8, 9, 14], "over": [], "avoid": [0, 5, 6, 9, 13], "alreadi": 9, "low": 9, "implment": [], "nuanc": 3, "detail": [0, 1, 2, 3, 4, 8, 9, 11, 14], "sevic": [], "ui": [], "No": 12, "properli": 1, "normal": [], "cours": [], "event": [], "relev": 6, "polymorph": [], "getter": [], "setter": [], "pair": [8, 14], "track": [], "correct": 8, "data": [0, 2, 3, 6, 8, 10, 12], "On": [], "easiest": [], "copi": 0, "past": [], "across": [], "board": [], "hierchi": [], "technolog": [], "base": [0, 1, 2, 3, 5, 6, 8, 11, 13, 14], "meta": 0, "driven": [], "cannot": [], "share": 11, "fiddl": [], "later": [], "acquir": [], "execut": [], "inject": [], "some_project": [], "singleton": [], "subsidiari": [], "propag": [], "select": [], "down": 3, "anoth": [], "accept": 11, "paramet": [9, 11, 13], "travers": 8, "problem": [], "forc": [], "solut": [0, 5], "consider": [3, 14], "script": 11, "assign": 6, "piec": 8, "parent": [1, 8, 14], "children": 8, "attach": [], "great": [], "deal": [], "dure": 9, "slow": [], "rare": 9, "speed": [], "achiev": [], "its": [], "entireti": [], "still": [], "overal": [0, 5, 8, 9], "enclos": [], "out": [6, 11], "clone": [], "parentag": [], "expand": [], "help": [0, 1, 12], "aren": [1, 9], "expect": 6, "sequenti": [], "scheme": [], "renumb": [], "visitor": 8, "after": 6, "integ": [], "memori": [], "multi": [], "becaus": [0, 3, 6, 12, 14], "reconstruct": 11, "unless": [], "irrespect": [], "loopnam": [], "loopoccur": [], "significantli": [], "undesir": [], "nest": [0, 4, 14], "bracket": [], "give": [], "loopseq": [], "try": [], "new": [], "fall": [], "apart": [], "absolut": [], "keep": [], "them": 6, "again": [], "fetch": [], "behav": [], "reassign": [], "compon": [2, 6, 9, 10, 11, 12, 14], "ascend": [], "meaningless": [], "surrog": [], "inadvert": [], "ident": [], "updat": [], "space": [], "rang": [], "barrier": [], "exemplifi": [], "long": [5, 6, 8], "stand": [], "cope": [], "superclass": 8, "abstract": [0, 8, 9], "concret": [], "alloc": [], "shown": [], "figur": 6, "x12structur": [], "mixtur": [], "target": [8, 11], "union": 8, "choic": 6, "subloop": [], "fairli": 0, "go": [], "degener": [], "exactli": 8, "doe": 9, "subloop_set": [], "iter": [8, 9], "child": [], "mix": [], "append": [], "put": [], "deger": [], "constraint": [], "appeal": [], "isn": [1, 8], "practic": [], "straight": [], "guidanc": [], "flatten": 8, "def": [], "previsit": [], "self": [2, 9, 13], "anod": [], "pass": [], "postvisit": [], "avisitor": [], "ii": [], "Then": 6, "descend": [], "until": [], "reach": [], "bottom": 9, "trick": [], "post": 8, "occasioanl": [], "sub": [1, 5, 6, 8, 9], "sure": 8, "expos": 8, "http": [8, 12, 14], "rest": [], "treat": [], "wa": [], "index": [10, 14], "typic": [], "experi": [], "ignor": [], "four": 1, "delet": [], "front": 6, "listen": [], "pr": [], "immedi": [], "behind": [], "mod_wsgi": [], "secur": [], "session": [], "cooki": [], "digest": [], "authent": [], "middlewar": [], "authkit": [], "org": [], "lukearno": [], "com": [8, 12, 14], "barrel": [], "401": [], "repli": [], "cycl": [], "nonc": [], "challenc": [], "consist": 6, "3rd": [], "forgerock": [], "openam": [], "establish": [], "sensibl": [0, 8], "extra": [], "standardseg": [], "sampl": 11, "actor": 10, "design": [1, 2, 5, 10, 13, 14], "summari": [8, 10], "appendix": 10, "search": [8, 10, 13], "effici": [], "storag": 12, "modif": 12, "purpos": 12, "270": [0, 1, 2, 8, 12, 14], "intermedi": 12, "notat": [0, 11, 12, 14], "json": [1, 2, 3, 5, 8, 9, 10, 12, 14], "preserv": [1, 3], "punctuat": [6, 9], "entiti": 14, "person": 14, "_": [], "ig": [1, 14], "compris": 14, "syntax": [1, 8, 14], "usag": [1, 8, 13, 14], "repetit": 14, "factor": 14, "4010": [8, 14], "x092": [8, 14], "a1": [8, 14], "github": [8, 13, 14], "azon": [8, 14], "master": [8, 14], "jsonschema": [8, 9, 14], "namespac": [0, 1, 2, 4, 8, 10, 14], "disambigu": [0, 8, 14], "appear": [0, 6, 9, 14], "mani": [8, 14], "msg_270_4010_x092_a1": [11, 14], "msg270": [0, 1, 2, 11, 14], "open": 14, "a_fil": [], "r": [1, 2, 3, 8, 13], "isa_loop": [0, 1, 2, 5, 9, 14], "isa_loop_isa": [1, 2, 5, 9, 14], "isa01": [0, 2, 5, 9, 14], "isa02": 2, "healthcar": 14, "oten": 14, "submiss": 14, "some_loop": [], "s01": [], "20230223": 14, "intent": 14, "deepli": [0, 5], "dump": [0, 11, 14], "w": 14, "print": [11, 14], "offer": 14, "pydant": 14, "atom": [1, 3, 6, 8, 9, 14], "x12composit": [], "dom": [], "suit": [], "wich": [], "perhap": 1, "borrow": [], "py12": [], "repositori": 14, "datael": [8, 14], "realist": 14, "depict": [6, 14], "segmentx": [0, 14], "signific": 14, "context": [0, 8, 10, 12], "question": 14, "topic": 14, "pyx12_extract": [], "plai": [], "some_messag": 0, "loop1": 0, "loop2": 0, "path": [0, 8, 9, 11, 13, 14], "referenc": 0, "defint": [1, 2], "messagea": [], "byte": [], "proprietari": 0, "freeli": 0, "obscur": [], "proce": [], "tibco": 0, "msg_mmm_vvvv_xxxx": 0, "isol": [], "suffici": 5, "idea": [0, 5, 8], "titl": [0, 1, 3], "227": 0, "descript": [0, 1, 2, 8], "gs_loop": [0, 1, 2, 14], "qualifi": [0, 1, 2, 4], "datatyp": [0, 1, 2, 5, 9], "i01": [0, 2, 5], "x12_type": 0, "minlength": [0, 1, 2, 8], "maxlength": [0, 1, 2, 8], "worst": 0, "vast": 0, "isa03": 2, "isa04": 2, "isa05": 2, "isa06": 2, "isa07": 2, "isa08": 2, "isa09": 2, "isa10": 2, "isa11": 2, "isa12": [2, 8], "isa13": 2, "isa14": 2, "isa15": 2, "isa16": [2, 6, 9, 14], "isa_loop_ta1": [1, 2], "isa_loop_iea": [1, 2, 3, 5], "inquiri": [0, 1, 2], "x092a1": [0, 1, 2], "ele_num": [2, 8], "data_typ": [2, 8], "inspect": 2, "get_annot": 2, "examin": [1, 2, 9], "annot": [1, 2, 3, 4, 9, 10, 13], "special": [2, 9], "carri": [2, 3], "dt": [2, 3, 8], "tm": [2, 3, 8], "nx": [2, 3], "suppli": [], "prefix": [4, 9], "potenti": [3, 5, 9], "radic": 5, "discard": 5, "With": [5, 6], "sens": 5, "msg_xxx": 5, "__init__": 5, "buri": [0, 5], "deep": 5, "directori": [5, 11], "break": [0, 5, 6], "zen": 5, "advic": 5, "better": [3, 5], "2100": 5, "2000": [0, 5], "loop_2100": 5, "express": [5, 11], "conceptu": [5, 6, 9], "isa_loop_isa01": [5, 9, 14], "now": [5, 9], "aspect": [1, 5], "tecchniqu": 5, "extract": [0, 8, 9, 11], "full": 8, "nnn": 8, "nnnn": 8, "xnnnn": 8, "detael": 8, "00401": 8, "00501": 8, "perfectli": [1, 3, 8], "around": [6, 8], "point": [8, 11], "understood": 8, "dataclass": 8, "capabl": 8, "incorpor": [1, 8], "explicitli": [8, 9], "some_cod": 8, "some_element_schema": 8, "parallel": 8, "uri": 8, "todo": 10, "bulk": 9, "written": [], "han": [], "codeset": 8, "str": [3, 8, 9, 13], "data_el": [1, 8], "enumer": 8, "enum": [1, 8], "xid": [0, 1, 8], "seq": 8, "refd": [1, 8], "inlin": 8, "min_len": [1, 8], "none": [1, 8, 9], "max_len": [1, 8], "common_def": 8, "ye": 8, "local": [8, 13], "code_set": 8, "percol": 8, "emitpython": 8, "po": [8, 9], "messagevisitor": 8, "schemamap": 8, "icvn": 8, "vriic": 8, "fic": 8, "abbr": 8, "end_tag": 8, "max_us": 8, "code_read": 8, "source_path": 14, "blob": 8, "rng": 8, "relaxng": 8, "approxim": 8, "arrai": [1, 6, 8, 9, 13], "20": 8, "6": [1, 3, 8], "eff_dt": 8, "stringh": 8, "element_read": 8, "tag": 8, "max": 8, "length": [3, 8, 9], "4": [1, 3, 8], "n": [1, 3, 8], "n0": [1, 3, 8], "n1": 8, "n2": [3, 8], "n5": 8, "n6": 8, "n7": 8, "n8": 8, "n9": 8, "16384": 8, "main": 8, "map_read": 8, "xsd": 8, "distinguish": [1, 8], "gs01": 8, "releas": 8, "industri": 8, "gs08": 8, "message_read": 8, "dict": [], "lot": 8, "henc": 8, "valid_cod": 8, "formattyp": [], "d8": 8, "yyyymmdd": 8, "d6": 8, "yymmdd": 8, "rd8": 8, "hhmm": 8, "usagetyp": [], "syntaxtyp": [], "l": 8, "p": 8, "c": 8, "9": [3, 8], "specifi": 8, "digit": 8, "distribut": [], "realli": [1, 6], "invari": 9, "start": [6, 9], "element_sep": 9, "unpack": 9, "compress": [6, 9], "yet": 9, "loop_namespac": [], "rich": 12, "wide": [1, 9, 12], "varieti": [0, 10, 12], "explor": [1, 14], "msg_271_4010_x092_a1": 14, "pathlib": [8, 11, 14], "cwd": 14, "271": [6, 14], "txt": [11, 14], "read_text": [11, 14], "msg271": 14, "00": [9, 14], "isa_loop_isa16": [9, 14], "st_loop": 14, "st_loop_st": 14, "st01": 14, "st_loop_st01": 14, "st02": 14, "st_loop_st02": 14, "0001": [6, 14], "header_bht": 14, "bht01": 14, "header_bht01": 14, "0022": 14, "bht02": 14, "header_bht02": 14, "11": 14, "bht03": 14, "header_bht03": 14, "11111": 14, "bht04": 14, "header_bht04": 14, "20120605": 14, "bht05": 14, "header_bht05": 14, "232423": 14, "changed_for_todai": 14, "xml_extract": [0, 9, 11, 13], "l2000_hl": 5, "l2100_hl": 5, "l2000": 5, "l2100": 5, "algorithm": [4, 6, 10], "charact": [6, 9], "choos": [6, 9], "former": 6, "split": [6, 9, 13], "segment_text": 6, "segment_class": 6, "build_attr": 6, "pragmat": 6, "bit": 2, "ll": [1, 11, 12], "easier": 1, "analyz": 1, "facilit": 1, "alwai": 1, "deduc": 1, "docstr": [1, 3, 13], "Is": [1, 3, 6], "obviou": 1, "reduc": [1, 13], "relianc": [1, 13], "taken": 1, "sill": 1, "30": [1, 3], "liter": [1, 3, 9], "iea01": [1, 3], "isa_loop_iea01": 1, "iea02": [1, 3], "isa_loop_iea02": 1, "segment_nam": [1, 3, 9], "immut": 1, "mutabl": 1, "sort": 1, "i16": [1, 3], "5": [1, 3, 13], "scale": [1, 3, 9], "data_type_cod": [1, 3], "were": 1, "l2110d_c003": 1, "c003": 1, "eq02_01": 1, "eq02": 1, "01": 1, "235": 1, "allof": 1, "cj": 1, "hc": 1, "iv": 1, "zz": 1, "eq02_02": 1, "02": 1, "234": 1, "eq02_03": 1, "03": [1, 9], "1339": 1, "eq02_04": 1, "04": 1, "eq02_05": 1, "05": 1, "eq02_06": 1, "06": 1, "eq02_07": 1, "07": 1, "352": 1, "7": 1, "l2110d_eq02_01": 1, "l2110d_eq02_02": 1, "l2110d_eq02_03": 1, "l2110d_eq02_04": 1, "l2110d_eq02_05": 1, "l2110d_eq02_06": 1, "six": 1, "2210d": 1, "consum": [6, 9], "scanner": [6, 9], "peek": [6, 9], "head": 6, "next": [6, 9, 13], "decid": 6, "finish": 6, "fewer": 6, "progress": 1, "fulli": 1, "introduc": [1, 3], "bug": 1, "wouldn": 1, "whether": 1, "much": 2, "primit": 2, "overhead": 3, "serial": [0, 3], "nativ": 3, "minlen": [3, 9], "maxlen": [3, 9], "y": 3, "datetim": 3, "h": 3, "m": 3, "exot": 3, "8": 3, "workabl": 3, "float": [3, 9], "size": [3, 9], "int": [3, 9], "decim": [3, 9], "almost": 3, "tini": 3, "typealia": 3, "strip": 3, "i12": 3, "c4": [0, 14], "suggest": [0, 14], "pretti": 0, "desktop": 0, "comput": 0, "back": 0, "lost": 0, "mixin": 0, "awar": 0, "m270_nav": 0, "bodi": 0, "major": 0, "area": 0, "c4model": 12, "unwis": 0, "fore": 14, "about": 14, "prohject": 14, "subtleti": 6, "found": 6, "convent": 6, "circular": 6, "mark": 6, "uncompress": 6, "106": [6, 9], "103": 6, "104": 6, "105": 6, "happen": 6, "fallback": 6, "hope": 6, "whitespac": [6, 9], "eyebal": 6, "separaror": 6, "16th": 6, "yucki": 6, "i15": 6, "nomin": 6, "everi": 6, "element_separ": 6, "834": [6, 9, 13], "2100a": [6, 9, 13], "2100b": [6, 9, 13], "dmg05": [6, 9, 13], "someth": 6, "val": 6, "component_separ": 6, "els": [6, 9, 11], "escap": 6, "pick": 6, "But": 6, "vari": 9, "oen": 9, "arg_dict": 9, "array_sep": 9, "souc": 9, "comp": 9, "osit": 9, "classmethod": 9, "attr_build": [9, 13], "field_typ": 9, "source_valu": 9, "popul": 9, "walk": 9, "segment_it": [9, 11], "basi": 9, "schematyp": 9, "embed": 9, "tricki": 9, "_segment_nam": 9, "element1": 9, "element3": 9, "everywher": 9, "indexerror": 9, "pop": 9, "empti": 9, "wrong": 9, "segment_sep": 9, "high": 9, "next_seg": 9, "let": 9, "advanc": 9, "textio": [8, 9, 13], "notabl": 9, "v": 9, "optim": [9, 13], "upcom": 9, "ahead": 9, "demo": 9, "2023": 9, "25": 9, "09": 9, "22": 9, "27": 9, "857661": 9, "thing": [11, 13], "you": 11, "rebuild": 11, "prefer": 11, "git": 11, "checkout": 11, "gather": 11, "anyth": 11, "dictionari": 11, "message_class": 11, "_kind": 11, "_name": 11, "__str__": 11, "nice": 11, "asdict": 11, "__repr__": 11, "repr": 11, "perspect": 8, "x12_packag": 8, "json_dir": 8, "make_jsonschema": 8, "make_python": 8, "entri": 13, "slott": 13, "tigershark3": 13, "90": 13, "doc": 13, "rst": 13, "86": 13, "144": 13, "190": 13, "28": 13, "dry": 13, "segment_walk": 13, "class_nam": 13, "below": 13, "faster": 13, "refactor": 13, "to_pi": 13, "hint": 13, "to_str": 13, "type_help": 13, "error": 13}, "objects": {"": [[8, 0, 0, "-", "tools"], [9, 0, 0, "-", "x12"]], "tools": [[8, 0, 0, "-", "xml_extract"]], "tools.xml_extract": [[8, 1, 1, "", "Codeset"], [8, 1, 1, "", "Composite"], [8, 1, 1, "", "DataElement"], [8, 1, 1, "", "Element"], [8, 1, 1, "", "EmitPython"], [8, 1, 1, "", "Loop"], [8, 1, 1, "", "Message"], [8, 1, 1, "", "MessageVisitor"], [8, 1, 1, "", "SchemaMap"], [8, 1, 1, "", "Segment"], [8, 2, 1, "", "code_reader"], [8, 2, 1, "", "element_reader"], [8, 2, 1, "", "main"], [8, 2, 1, "", "make_jsonschema"], [8, 2, 1, "", "make_python"], [8, 2, 1, "", "map_reader"], [8, 2, 1, "", "message_reader"]], "x12": [[9, 0, 0, "-", "base"], [9, 0, 0, "-", "common"]], "x12.base": [[9, 1, 1, "", "Composite"], [9, 1, 1, "", "Element"], [9, 1, 1, "", "Loop"], [9, 1, 1, "", "Message"], [9, 1, 1, "", "SchemaType"], [9, 1, 1, "", "Segment"], [9, 1, 1, "", "Source"], [9, 2, 1, "", "demo"]], "x12.base.Composite": [[9, 3, 1, "", "attr_build"]], "x12.base.Element": [[9, 4, 1, "", "value"]], "x12.base.Loop": [[9, 3, 1, "", "attr_build"], [9, 3, 1, "", "segment_iter"]], "x12.base.Message": [[9, 3, 1, "", "segment_iter"]], "x12.base.Segment": [[9, 3, 1, "", "attr_build"], [9, 3, 1, "", "elements"], [9, 3, 1, "", "parse"]], "x12.base.Source": [[9, 3, 1, "", "elements"], [9, 3, 1, "", "next_segment"], [9, 3, 1, "", "peek"]]}, "objtypes": {"0": "py:module", "1": "py:class", "2": "py:function", "3": "py:method", "4": "py:property"}, "objnames": {"0": ["py", "module", "Python module"], "1": ["py", "class", "Python class"], "2": ["py", "function", "Python function"], "3": ["py", "method", "Python method"], "4": ["py", "property", "Python property"]}, "titleterms": {"architectur": 0, "design": [0, 3, 4, 9], "summari": 0, "meta": [], "level": [], "process": 0, "x12": [0, 8, 9, 10, 11, 14], "background": [], "messag": [0, 1, 6, 8, 11, 14], "definit": [0, 5, 8], "applic": 0, "databas": [], "altern": [], "persist": [], "choic": [], "flat": [], "text": [], "segment": [1, 6, 11], "type": [1, 8], "base": 9, "gener": 6, "orm": [], "detail": [], "compon": 0, "model": [0, 2, 14], "manipul": [], "unmarshal": [0, 14], "present": [], "queri": [], "marshal": [0, 14], "data": 14, "appendix": 0, "i": 0, "note": 4, "reconcil": [], "bare": [], "python": 11, "class": [2, 3, 5, 11], "django": [], "problem": [], "forc": [], "solut": [], "consequ": [], "batch": [], "script": [], "custom": [], "structur": [8, 14], "kei": [], "x12messag": [], "us": [11, 14], "case": 14, "recurs": [], "sql": [], "travers": [], "visitor": [], "In": [], "order": [], "traver": [], "depth": [], "first": [], "pre": [], "web": [], "servic": [], "port": [], "url": [], "s": 0, "claim": [], "modul": 5, "extra": [], "standardseg": [], "implement": 7, "test": [], "packag": [5, 8, 9], "tool": [8, 10], "project": [], "tiger": 10, "shark": 10, "indic": 10, "tabl": 10, "overview": 12, "actor": 14, "scenario": 14, "creat": 11, "A": 14, "factori": [], "builder": [], "xml": [], "schema": [0, 8, 11], "defin": 14, "an": [6, 14], "defint": [], "json": [0, 11], "loop": [1, 5], "namespac": 5, "nest": 5, "qualifi": 5, "name": [5, 8], "prefix": 5, "sourc": 8, "typd": [], "version": 8, "map": 8, "pyx12_extract": [], "pars": [6, 11], "exchang": [6, 11], "format": [6, 11], "annot": [], "todo": [1, 8, 9, 13], "element": [1, 3], "composit": 1, "hint": 1, "develop": 0, "view": 0, "contain": 0, "layer": [], "context": 14, "perspect": 0, "depend": 14, "common": 9, "tigershark": 11, "emit": 11, "varieti": 11, "sequenc": 11, "output": 11, "xml_extract": 8, "The": 13, "list": 13}, "envversion": {"sphinx.domains.c": 2, "sphinx.domains.changeset": 1, "sphinx.domains.citation": 1, "sphinx.domains.cpp": 6, "sphinx.domains.index": 1, "sphinx.domains.javascript": 2, "sphinx.domains.math": 2, "sphinx.domains.python": 3, "sphinx.domains.rst": 2, "sphinx.domains.std": 2, "sphinx.ext.todo": 2, "sphinx": 56}})