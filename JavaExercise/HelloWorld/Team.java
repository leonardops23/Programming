package JavaExercise.HelloWorld;

public class Team {
    Member member;

    public Team(Member member) {
        this.member = member;
    }

    public static void main (String[] args) {
        Member myMember = new Member("Messi", "DM", 10, 89, 90);
        Team myTeam = new Team(myMember);
        System.out.println(myTeam.member.getName());
        System.out.println(myTeam.member.getPosition());
        System.out.println(myTeam.member.getDorsal());
        System.out.println(myTeam.member.getLevel());
        System.out.println(myTeam.member.getRank());
    }
}

class Member {
    private String name;
    private String position;
    private int dorsal;
    private int level;
    private int rank;

    public Member(String name, String position, int dorsal, int level, int rank) {
        this.name = name;
        this.position = position;
        this.dorsal = dorsal;
        this.level = level;
        this.rank = rank;
    }

    public String getName() {
        return this.name;
    }

    public String getPosition() {
        return this.position;
    }

    public int getDorsal() {
        return this.dorsal;
    }

    public int getLevel() {
        return this.level;
    }

    public int getRank() {
        return this.rank;
    }
}
