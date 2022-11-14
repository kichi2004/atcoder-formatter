// ==UserScript==
// @name           AtCoder Formatter
// @name:en        AtCoder Formatter
// @namespace
// @version        1.3.0
// @description    AtCoder の解説コードなどをフォーマットできるようにします．
// @description:en Add formatting buttons to source codes on AtCoder.
// @author         kichi2004
// @match          https://atcoder.jp/contests/*
// @grant          none
// @updateURL      https://raw.githubusercontent.com/kichi2004/atcoder-formatter/master/user_script/script.js
// @downloadURL    https://raw.githubusercontent.com/kichi2004/atcoder-formatter/master/user_script/script.js
// @namespace      kichi2004.jp
// @license        MIT
// ==/UserScript==

'use strict';

(async function () {

    const formatCode = async (event, pre, id, lang) => {
        const removeModal = () => {
            $(`#modal-${id}-format-warning`).modal('hide')
        }

        const formatInner = async (modal = false) => {
            if (modal) {
                removeModal()
            }

            event.target.disabled = true
            const data = document.getElementById(id)
            const res = await fetch(`https://formatter.api.kichi2004.jp/format?lang=${lang}`, {
                body: data.innerText,
                method: 'POST'
            })
            event.target.disabled = false
            if (!res.ok) {
                alert('Formatting Request Failed!')
                return
            }
            const json = await res.json()
            if (json['status'] === 'error') {
                alert('Formatting Error!\n' + json['error'])
                return
            }
            const result = json['result']
            const nextPre = document.createElement('pre')
            nextPre.textContent = result
            nextPre.classList.add('prettyprint', `lang-${lang}`, 'linenums')
            pre.before(nextPre)
            pre.remove()

            data.textContent = result
            PR.prettyPrint()
        }

        const finished = endTime.toDate() < new Date()
        if (finished) {
            await formatInner()
            return
        }

        document.body.insertAdjacentHTML('afterbegin', `
<div id="modal-${id}-format-warning" class="modal fade" tabindex="-1" role="dialog">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">フォーマットの注意</h4>
            </div>
            <div class="modal-body">
                <p>このコンテストはまだ終了していません。</p>
                <p>フォーマットを行うとソースコードが外部に送信され、スクリプトの作成者が閲覧可能な状態になります。</p>
                <p>まだ公開されていないコンテストではフォーマットを行わないでください。</p>
            </div>
            <div class="modal-footer">
                <button class="btn btn-warning" id="${id}-force-format">フォーマットする</button>
                <button class="btn btn-success" id="${id}-cancel">キャンセル</button>
            </div>
        </div>
    </div>
</div>
        `)

        $(`#modal-${id}-format-warning`).modal('show')
        document.getElementById(`${id}-force-format`).addEventListener('click', async () => await formatInner(true))
        document.getElementById(`${id}-cancel`).addEventListener('click', removeModal)
    }

    for (const pre of document.getElementsByClassName('prettyprint')) {
        const next = pre.nextElementSibling
        if (next.className !== 'source-code-for-copy') continue
        const id = next.id

        let adding = pre.previousElementSibling
        while (adding.className === 'div-btn-copy')
            adding = adding.previousElementSibling

        const buttonClass = endTime.toDate() < new Date() ? 'btn-info' : 'btn-danger'

        adding.insertAdjacentHTML(
            'afterend',
            `
<div class="btn-group" role="group">
    <button type="button" class="btn ${buttonClass} btn-sm" >
        C++
    </button>
    <button type="button" class="btn ${buttonClass} btn-sm" id="${id}-fmt-py">
        Python
    </button>
    <button type="button" class="btn ${buttonClass} btn-sm" id="${id}-fmt-cs">
        C#
    </button>
</div>`
        )
        for (const lang of ['cpp', 'py', 'cs']) {
            document.getElementById(`${id}-fmt-${lang}`)
                .addEventListener('click', async (e) => await formatCode(e, pre, id, lang))
        }
    }
})()
