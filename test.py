import os
import json
from path2tree import Path2Tree


if __name__ == '__main__':
	file_list = []
	for root, dirs, files in os.walk("TEST"):
		for file in files:
			file_path = os.path.join(root, file)
			file_list.append(file_path)

	p2t = Path2Tree(file_list)
	print(json.dumps(file_list, indent=4))
	print("--------->")
	print(p2t.get_tree())