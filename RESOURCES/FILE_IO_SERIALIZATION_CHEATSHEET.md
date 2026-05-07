# File I/O & Serialization Cheat Sheet

## 1. BASIC FILE OPERATIONS

### Read File
```python
with open(filename, "r", encoding="utf-8") as f:
    content = f.read()  # Returns entire file as string
```

### Write File
```python
with open(filename, "w", encoding="utf-8") as f:
    f.write(text)  # Overwrites file, returns chars written
```

### Append to File
```python
with open(filename, "a", encoding="utf-8") as f:
    f.write(text)  # Appends to file, doesn't overwrite
```

---

## 2. JSON (Human-readable, text format)

### Serialize: Python object → JSON string
```python
import json

data = {"name": "John", "age": 25}
json_string = json.dumps(data)  # Returns: '{"name": "John", "age": 25}'
print(type(json_string))  # <class 'str'>
```

### Serialize & Save: Python object → JSON file
```python
import json

data = {"name": "John", "age": 25}
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f)  # Writes directly to file
```

### Deserialize: JSON string → Python object
```python
import json

json_string = '{"name": "John", "age": 25}'
data = json.loads(json_string)  # Returns dict
print(type(data))  # <class 'dict'>
```

### Deserialize & Load: JSON file → Python object
```python
import json

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)  # Reads from file and converts
print(type(data))  # <class 'dict'>
```

### JSON Quick Reference
| Method | Input | Output | Use When |
|---|---|---|---|
| `json.dumps()` | Python object | JSON string | Converting to string |
| `json.dump()` | Python object + file | Writes to file | Saving to file |
| `json.loads()` | JSON string | Python object | Converting string to object |
| `json.load()` | file | Python object | Reading from file |

**Memory trick:** `s` = String (dumps/loads), no `s` = File (dump/load)

---

## 3. CSV (Tabular data, comma-separated)

### Read CSV → List of Dictionaries
```python
import csv

data = []
with open("data.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)  # Each row becomes a dict
    for row in reader:
        data.append(row)
        # row = {'name': 'John', 'age': '25', 'city': 'New York'}

print(type(data))  # <class 'list'>
print(type(data[0]))  # <class 'dict'>
```

### Read CSV (all at once)
```python
import csv

with open("data.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    data = list(reader)  # Convert to list immediately
```

### Write Dictionary to CSV
```python
import csv

data = [
    {'name': 'John', 'age': 25},
    {'name': 'Jane', 'age': 30}
]

with open("data.csv", "w", encoding="utf-8") as f:
    fieldnames = ['name', 'age']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()  # Write column headers
    writer.writerows(data)  # Write all rows
```

### CSV Key Points
- **First row** = column headers (name, age, city)
- **Other rows** = data
- `DictReader` converts rows to dictionaries
- `DictWriter` writes dictionaries as rows

---

## 4. PICKLE (Binary format, preserves Python objects)

### Save Object to File
```python
import pickle

obj = MyClass("John", 25, True)
with open("object.pkl", "wb") as f:  # "wb" = write binary
    pickle.dump(obj, f)  # Save entire object
```

### Load Object from File
```python
import pickle

with open("object.pkl", "rb") as f:  # "rb" = read binary
    obj = pickle.load(f)  # Load object back
print(type(obj))  # <class '__main__.MyClass'>
```

### Pickle in a Class
```python
import pickle

class CustomObject:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def serialize(self, filename):
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
            return True
        except Exception:
            return False
    
    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception:
            return None
```

### Pickle vs JSON
| Feature | Pickle | JSON |
|---|---|---|
| Format | Binary (not human-readable) | Text (human-readable) |
| Can save | Any Python object | Only basic types (dict, list, str, int, bool) |
| File mode | `"wb"` / `"rb"` | `"w"` / `"r"` |
| Use pickle.dump/load | pickle.dump(obj, f) | json.dump(data, f) |

---

## 5. XML (Hierarchical, tag-based format)

### Serialize: Dict → XML File
```python
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    try:
        root = ET.Element("data")
        
        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)  # Convert to string
        
        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8")
        return True
    except Exception:
        return False

# Usage
data = {"name": "John", "age": "25"}
serialize_to_xml(data, "data.xml")
```

### Deserialize: XML File → Dict
```python
import xml.etree.ElementTree as ET

def deserialize_from_xml(filename):
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        
        dictionary = {}
        for child in root:
            dictionary[child.tag] = child.text
        
        return dictionary
    except Exception:
        return None

# Usage
data = deserialize_from_xml("data.xml")
```

### XML Output Example
```xml
<data>
    <name>John</name>
    <age>25</age>
</data>
```

### XML Key Points
- `ET.Element()` = create root element
- `ET.SubElement()` = create child element
- `child.text` = set element value
- `ET.parse()` = read XML file
- `getroot()` = get root element
- Everything is stored as **STRING** (convert types manually)

---

## 6. FILE MODES QUICK REFERENCE

| Mode | Creates File? | Overwrites? | Appends? | Use For |
|---|---|---|---|---|
| `"r"` | ❌ | ❌ | ❌ | Reading text |
| `"w"` | ✅ | ✅ | ❌ | Writing text |
| `"a"` | ✅ | ❌ | ✅ | Appending text |
| `"rb"` | ❌ | ❌ | ❌ | Reading binary (pickle) |
| `"wb"` | ✅ | ✅ | ❌ | Writing binary (pickle) |

---

## 7. ERROR HANDLING PATTERN

```python
def function(filename):
    try:
        # Your code here
        with open(filename, "r") as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"File {filename} not found")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
```

---

## 8. SERIALIZATION WORKFLOW

```
Python Object → Serialize → File Format → Deserialize → Python Object
     ↓              ↓              ↓             ↓              ↓
  MyClass      json.dump()      JSON         json.load()    dict
  MyClass      pickle.dump()    Binary       pickle.load()  MyClass
    dict      serialize_to_xml() XML      deserialize_from_xml() dict
```

---

## 9. COMMON CONVERSIONS

### List of dicts to JSON
```python
data = [{"name": "John"}, {"name": "Jane"}]
with open("file.json", "w") as f:
    json.dump(data, f)
```

### JSON to list of dicts
```python
with open("file.json", "r") as f:
    data = json.load(f)
```

### CSV to JSON
```python
import csv
import json

data = []
with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    data = list(reader)

with open("data.json", "w") as f:
    json.dump(data, f)
```

---

## 10. KEY TAKEAWAYS

✅ Use `with` statement (automatically closes file)
✅ Always specify `encoding="utf-8"`
✅ JSON: human-readable, basic types only
✅ CSV: tabular data
✅ Pickle: any Python object, binary format
✅ XML: hierarchical, all text (needs type conversion)
✅ Use try-except for file operations
✅ Binary modes: `"wb"` (write), `"rb"` (read)
