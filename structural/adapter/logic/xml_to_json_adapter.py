from __future__ import annotations

from typing import Dict, Any, List, TYPE_CHECKING

if TYPE_CHECKING:
    from xml.etree.ElementTree import Element


class XmlToJsonAdapter:
    def __init__(self, node: Element) -> None:
        self.node = node

    def convert_to_json(self) -> Dict[Any, Any]:
        converted_to_json = {}
        self._get_node_dict(self.node, converted_to_json)

        return converted_to_json

    def _get_node_dict(self, node: Element, parent_node_dict: Dict[Any, Any]):
        node_text = node.text.strip()

        if (children := list(node)) or not node_text:
            node_content = {}
        else:
            node_content = node_text

        parent_node_dict[node.tag] = node_content

        if children:
            unique_tags = self._get_unique_children_tags(children)
            non_unique_child_dict = {}
            current_node_dict = parent_node_dict.get(node.tag)

            for child in children:
                if child.tag in unique_tags:
                    self._get_node_dict(child, current_node_dict)
                else:
                    child_dict = {}
                    if non_unique_child_dict.get(child.tag) is None:
                        non_unique_child_dict[child.tag] = []

                    self._get_node_dict(child, child_dict)
                    non_unique_child_dict[child.tag].append(child_dict[child.tag])

            current_node_dict.update(non_unique_child_dict)

    @staticmethod
    def _get_children_tags(children: List[Element]):
        tags = []
        for child in children:
            tags.append(child.tag)

        return tags

    def _get_unique_children_tags(self, children: List[Element]):
        tags = self._get_children_tags(children)

        return [tag for tag in tags if tags.count(tag) == 1]
