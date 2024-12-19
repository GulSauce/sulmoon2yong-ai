from langchain_community.tools import DuckDuckGoSearchRun


from app.core.util.ai_manager import AIManager
from app.core.prompt.improve_user_prompt_with_searched_result_prompt import (
    improve_user_prompt_with_searched_result_prompt,
)
from app.core.prompt.find_keyword_prompt import find_keyword_prompt
from duckduckgo_search.exceptions import DuckDuckGoSearchException


NOT_TO_NEED_SEARCH_STRING = "NOT_TO_NEED_SEARCH"


def chat_improve_user_prompt_with_search(ai_manager: AIManager, user_prompt):
    if user_prompt == "":
        return

    keyword = ai_manager.chat(find_keyword_prompt.format(user_prompt=user_prompt))

    print(f"keyword: {keyword}")

    if keyword == NOT_TO_NEED_SEARCH_STRING:
        return user_prompt

    search = DuckDuckGoSearchRun()

    try:
        searched_result = search.invoke(keyword)
    except Exception as e:
        print(f"Search error occurred: {e}")
        return user_prompt

    result = user_prompt + "\nreference)\n" + searched_result
    print(f"result: {result}")
    return result


async def async_chat_improve_user_prompt_with_search(
    ai_manager: AIManager, user_prompt
):
    if user_prompt == "":
        return

    keyword = await ai_manager.async_chat(
        find_keyword_prompt.format(user_prompt=user_prompt)
    )

    print(f"keyword: {keyword}")

    if keyword == NOT_TO_NEED_SEARCH_STRING:
        return user_prompt

    search = DuckDuckGoSearchRun()

    searched_result = await search.ainvoke(keyword)

    print(f"searched_result: {searched_result}")

    result = user_prompt + "\nreference)\n" + searched_result
    print(f"result: {result}")
    return result
