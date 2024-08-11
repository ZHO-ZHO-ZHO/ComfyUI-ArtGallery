import os
import folder_paths

#uploadimg
def modify_js_file(file_path, new_content):
    with open(file_path, 'r') as file:
        content = file.read()

    # 检查文件中是否已包含需要添加的内容
    if "image_upload_artist" not in content:
        # 找到原始代码的位置
        insert_position = content.find('nodeData.input.required.upload = ["IMAGEUPLOAD"];')
        if insert_position != -1:
            # 在原始代码后插入新的代码
            insert_position += len('nodeData.input.required.upload = ["IMAGEUPLOAD"];')
            content = content[:insert_position] + new_content + content[insert_position:]

            # 写回文件
            with open(file_path, 'w') as file:
                file.write(content)
            print(f"File '{file_path}' updated successfully.✅")
        else:
            print("Original code block not found.❌")
    else:
        print("File already contains the necessary modifications.✅")

# 要插入的新内容
new_js_content = """
		}
		// 检查艺术家图像上传
		if (nodeData?.input?.required?.image?.[1]?.image_upload_artist === true) {
			nodeData.input.required.upload = ["ARTISTS_IMAGEUPLOAD"];
		}
		// 检查相机图像上传
		if (nodeData?.input?.required?.image?.[1]?.image_upload_camera === true) {
			nodeData.input.required.upload = ["CAMERAS_IMAGEUPLOAD"];
		}
		// 检查胶片图像上传
		if (nodeData?.input?.required?.image?.[1]?.image_upload_film === true) {
			nodeData.input.required.upload = ["FILMS_IMAGEUPLOAD"];
		}
		// 检查艺术运动图像上传
		if (nodeData?.input?.required?.image?.[1]?.image_upload_movement === true) {
			nodeData.input.required.upload = ["MOVEMENTS_IMAGEUPLOAD"];
		}
		// 检查风格图像上传
		if (nodeData?.input?.required?.image?.[1]?.image_upload_style === true) {
			nodeData.input.required.upload = ["STYLES_IMAGEUPLOAD"];

"""

# 文件路径
current_dir = os.path.dirname(os.path.abspath(__file__))
uploadimg_js_file_path = os.path.join(folder_paths.base_path, 'web/extensions/core/uploadImage.js')
print(uploadimg_js_file_path)

modify_js_file(uploadimg_js_file_path, new_js_content)


#folderpath
def modify_py_file(file_path, new_content, search_line, function_content, search_function):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # 准备新内容和函数内容的关键行用于比较
    new_content_key_line = new_content.strip().split('\n')[0]
    function_content_key_line = function_content.strip().split('\n')[0]

    # 检查新内容是否已存在
    if new_content_key_line not in "".join(lines):
        for index, line in enumerate(lines):
            if search_line in line:
                lines.insert(index + 1, new_content)
                break

    # 检查函数修改是否已存在
    if function_content_key_line not in "".join(lines):
        function_start = False
        for index, line in enumerate(lines):
            if search_function in line:
                function_start = True
            if function_start and "return None" in line:
                lines.insert(index, function_content)
                break

    # 写回文件
    with open(file_path, 'w') as file:
        file.writelines(lines)
    print(f"File '{file_path}' updated successfully.✅")

# 要插入的新内容
new_py_content = """
supported_artist_extensions = [".jpg", ".png", ".jpeg"]
artists_dir = os.path.join(base_path, "custom_nodes", "ComfyUI-ArtGallery", "img_lists", "artists")
folder_names_and_paths["artists"] = ([artists_dir], supported_artist_extensions)

cameras_dir = os.path.join(base_path, "custom_nodes", "ComfyUI-ArtGallery", "img_lists", "cameras")
folder_names_and_paths["cameras"] = ([cameras_dir], supported_artist_extensions)

films_dir = os.path.join(base_path, "custom_nodes", "ComfyUI-ArtGallery", "img_lists", "films")
folder_names_and_paths["films"] = ([films_dir], supported_artist_extensions)

movements_dir = os.path.join(base_path, "custom_nodes", "ComfyUI-ArtGallery", "img_lists", "movements")
folder_names_and_paths["movements"] = ([movements_dir], supported_artist_extensions)

styles_dir = os.path.join(base_path, "custom_nodes", "ComfyUI-ArtGallery", "img_lists", "styles")
folder_names_and_paths["styles"] = ([styles_dir], supported_artist_extensions)
"""

# 要修改的函数内容
function_py_content = '''\
    if type_name == "artists":
        return folder_names_and_paths["artists"][0][0]
    if type_name == "cameras":
        return folder_names_and_paths["cameras"][0][0]
    if type_name == "films":
        return folder_names_and_paths["films"][0][0]
    if type_name == "movements":
        return folder_names_and_paths["movements"][0][0]
    if type_name == "styles":
        return folder_names_and_paths["styles"][0][0]
'''


# 文件路径

py_file_path = os.path.join(folder_paths.base_path, 'folder_paths.py')

modify_py_file(py_file_path, new_py_content, 'folder_names_and_paths["classifiers"]', function_py_content, 'def get_directory_by_type(type_name):')


#wedget
def modify_wedgets_js_file(file_path, new_content, new_content_2):
    with open(file_path, 'r') as file:
        content = file.read()

    # 检查文件中是否已包含需要添加的内容
    if "ARTISTS_IMAGEUPLOAD" not in content:
        # 找到原始代码的位置
        insert_position = content.find('return (display==="slider") ? "slider" : "number"')
        if insert_position != -1:
            # 在原始代码后插入新的代码
            insert_position += len('return (display==="slider") ? "slider" : "number"')
            content = content[:insert_position] + new_content + content[insert_position:]

        insert_position_2 = content.find('return { widget: uploadWidget };')
        if insert_position_2 != -1:
            # 在原始代码后插入新的代码
            insert_position_2 += len('return { widget: uploadWidget };')
            content = content[:insert_position_2] + new_content_2 + content[insert_position_2:]

            # 写回文件
            with open(file_path, 'w') as file:
                file.write(content)
            print(f"File '{file_path}' updated successfully.✅")
        else:
            print("Original code block not found.❌")
    else:
        print("File already contains the necessary modifications.✅")

# 要插入的新内容
new_wedgets_js_content = """
}

// 通用的图像上传函数
function createImageUploadWidget(node, inputName, inputData, imageType, app) {
	const imageWidget = node.widgets.find((w) => w.name === (inputData[1]?.widget ?? "image"));
	let AuploadWidget;

	function showImage(name, type) {
		const img = new Image();
		img.onload = () => {
			node.imgs = [img];
			app.graph.setDirtyCanvas(true);
		};
		let folder_separator = name.lastIndexOf("/");
		let subfolder = "";
		if (folder_separator > -1) {
			subfolder = name.substring(0, folder_separator);
			name = name.substring(folder_separator + 1);
		}
		img.src = api.apiURL(`/view?filename=${encodeURIComponent(name)}&type=${type}&subfolder=${subfolder}${app.getPreviewFormatParam()}${app.getRandParam()}`);
		node.setSizeForImage?.();
	}

	var default_value = imageWidget.value;
	Object.defineProperty(imageWidget, "value", {
		set: function (value) {
			this._real_value = value;
		},

		get: function () {
			let value = "";
			if (this._real_value) {
				value = this._real_value;
			} else {
				return default_value;
			}

			if (value.filename) {
				let real_value = value;
				value = "";
				if (real_value.subfolder) {
					value = real_value.subfolder + "/";
				}

				value += real_value.filename;

				if (real_value.type && real_value.type !== "input")
					value += ` [${real_value.type}]`;
			}
			return value;
		}
	});

	// 添加回调函数以在更改图像时渲染图像
	const cb = node.callback;
	imageWidget.callback = function () {
		showImage(imageWidget.value, imageType);
		if (cb) {
			return cb.apply(this, arguments);
		}
	};

	// 在加载时，如果有值，则渲染图像
	// 值不会立即设置，因此我们需要等待一会儿
	// 初始设置值时不会触发更改回调
	requestAnimationFrame(() => {
		if (imageWidget.value) {
			showImage(imageWidget.value, imageType);
		}
	});

	return { widget: AuploadWidget };
"""
new_wedgets_js_content_2 = """
	},
	ARTISTS_IMAGEUPLOAD(node, inputName, inputData, app) {
		return createImageUploadWidget(node, inputName, inputData, 'artists', app);
	},
	CAMERAS_IMAGEUPLOAD(node, inputName, inputData, app) {
		return createImageUploadWidget(node, inputName, inputData, 'cameras', app);
	},
	FILMS_IMAGEUPLOAD(node, inputName, inputData, app) {
		return createImageUploadWidget(node, inputName, inputData, 'films', app);
	},
	MOVEMENTS_IMAGEUPLOAD(node, inputName, inputData, app) {
		return createImageUploadWidget(node, inputName, inputData, 'movements', app);
	},
	STYLES_IMAGEUPLOAD(node, inputName, inputData, app) {
		return createImageUploadWidget(node, inputName, inputData, 'styles', app);
"""

# 文件路径
wedgets_js_file_path = os.path.join(folder_paths.base_path, 'web/scripts/widgets.js')

modify_wedgets_js_file(wedgets_js_file_path, new_wedgets_js_content, new_wedgets_js_content_2)


from .ArtGallery import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']