"""CreateBodiesTable Migration."""

from masoniteorm.migrations import Migration


class CreateBodiesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("bodies") as table:
            table.increments("id")
            table.string("name")
            table.string("date_discovered")
            table.string("details")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("bodies")
