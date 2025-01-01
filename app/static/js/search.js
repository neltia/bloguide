// 엔터 키 입력 처리
export function handleKeyPress(event) {
    if (event.key === "Enter") {
        search();
    }
}

// 검색 API 호출
export async function search() {
    const query = document.getElementById("search-input").value;
    if (!query) {
        alert("검색어를 입력해 주세요.");
        return;
    }

    try {
        const response = await fetch(`/api/markdown/search?query=${encodeURIComponent(query)}`);
        const result = await response.json();
        console.log(result);

        if (!result.data || !result.data.list) {
            alert("검색 결과가 없습니다.");
            return;
        }

        // 결과 렌더링
        renderResults(result);
    } catch (error) {
        console.error("검색 중 오류 발생:", error);
        alert("검색 중 문제가 발생했습니다.");
    }
}

// 검색 결과 렌더링
function renderResults(result) {
    const resultsDiv = document.getElementById("results");
    resultsDiv.innerHTML = ""; // 초기화

    if (result.result_code !== 200 || !result.data?.list) {
        resultsDiv.innerHTML = `<p class="text-gray-700">검색 결과가 없습니다.</p>`;
        return;
    }

    const items = result.data.list.map(
        (item) =>
            `<div class="p-4 border-b border-gray-300">
                <a href="${item.link}" class="text-blue-600 hover:underline">${item.title}</a>
            </div>`
    );

    resultsDiv.innerHTML = items.join("");
}
