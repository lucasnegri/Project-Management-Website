


function addMember(event, memberId, teamId) {
    window.location.href = "/manage_team/" + teamId + "/add_member/" + memberId;
}

function removeMember(event, memberId, teamId) {
    window.location.href = "/manage_team/" + teamId + "/remove_member/" + memberId;
}